"""Read-only FactBase MCP client with local credential configuration."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import urllib.request
from urllib.parse import urlparse

class KnowledgeClient:
    def __init__(self, config: Path):
        self.config = json.loads(config.read_text())
        if urlparse(self.config['url']).scheme != 'https': raise ValueError('Knowledge credentials require HTTPS')
        self.session = None
        self.counter = 0
    def request(self, method, params):
        self.counter += 1
        params = {**params, '_meta': {'io.modelcontextprotocol/protocolVersion':'2026-07-28','io.modelcontextprotocol/clientInfo':{'name':'ink-marketing-research','version':'1.0.0'},'io.modelcontextprotocol/clientCapabilities':{}}}
        headers = {'Authorization': 'Bearer ' + self.config['token'], 'Content-Type':'application/json', 'Accept':'application/json, text/event-stream', 'MCP-Protocol-Version':'2026-07-28', 'Mcp-Method':method}
        if method == 'tools/call': headers['Mcp-Name'] = params['name']
        if self.session: headers['Mcp-Session-Id'] = self.session
        body = json.dumps(dict(jsonrpc='2.0', id=self.counter, method=method, params=params)).encode()
        with urllib.request.urlopen(urllib.request.Request(self.config['url'], data=body, headers=headers), timeout=40) as response:
            self.session = response.headers.get('Mcp-Session-Id', self.session)
            raw=response.read().decode()
            if response.headers.get('Content-Type','').startswith('text/event-stream'):
                messages=[json.loads(line[5:].strip()) for line in raw.splitlines() if line.startswith('data:')]
                value=next(item for item in messages if item.get('id')==self.counter)
            else: value=json.loads(raw)
        if 'error' in value: raise RuntimeError(json.dumps(value['error']))
        return value['result']
    def initialize(self):
        return self.request('server/discover', {})
    def call(self, name, arguments):
        if name not in ('search','retrieve'): raise ValueError('Only read-only knowledge tools are allowed')
        return self.request('tools/call', {'name':name,'arguments':arguments})

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',type=Path,required=True)
    action=parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--list',action='store_true')
    action.add_argument('--query')
    action.add_argument('--retrieve',help='An exact ID returned by search')
    parser.add_argument('--selection',type=Path,help='Search selection JSON, including date and purpose')
    args=parser.parse_args()
    client=KnowledgeClient(args.config); client.initialize()
    result = client.request('tools/list',{}) if args.list else client.call('retrieve',{'id':args.retrieve}) if args.retrieve else client.call('search',{'query':args.query,'limit':5,**({'selection':json.loads(args.selection.read_text())} if args.selection else {})})
    print(json.dumps(result,ensure_ascii=False))
