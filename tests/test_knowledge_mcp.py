import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from knowledge_mcp import KnowledgeClient
class KnowledgeClientTests(unittest.TestCase):
    def test_refuses_plaintext_credentials_and_non_read_tools(self):
        with tempfile.TemporaryDirectory() as temp:
            config=Path(temp)/'config.json'
            config.write_text(json.dumps({'url':'http://example.com/mcp','token':'fictional'}))
            with self.assertRaises(ValueError):KnowledgeClient(config)
            config.write_text(json.dumps({'url':'https://example.com/mcp','token':'fictional'}))
            client=KnowledgeClient(config)
            with self.assertRaises(ValueError):client.call('write',{})
