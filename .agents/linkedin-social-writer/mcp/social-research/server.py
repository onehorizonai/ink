#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import tempfile
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from typing import Any


SERVER_NAME = "linkedin-social-research"
SERVER_VERSION = "0.1.0"
PROTOCOL_VERSION = "2024-11-05"
DEFAULT_USER_AGENT = "Mozilla/5.0 (compatible; InkBot/1.0; +https://github.com/onehorizonai/ink)"


TOOLS = [
    {
        "name": "web_search",
        "description": "Search the web for sources, references, or verification targets.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_results": {"type": "integer", "minimum": 1, "maximum": 10, "default": 5},
                "site": {"type": "string"},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "fetch_page",
        "description": "Fetch a URL and return readable text for claim review.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "max_chars": {"type": "integer", "minimum": 500, "maximum": 50000, "default": 12000},
            },
            "required": ["url"],
            "additionalProperties": False,
        },
    },
    {
        "name": "search_unsplash",
        "description": "Search Unsplash for candidate images and return photo and photographer links.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "per_page": {"type": "integer", "minimum": 1, "maximum": 30, "default": 6},
                "page": {"type": "integer", "minimum": 1, "default": 1},
                "orientation": {
                    "type": "string",
                    "enum": ["landscape", "portrait", "squarish"],
                },
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "google_trends_trending_searches",
        "description": "Fetch daily Google Trends search topics for a geography, with optional keyword filtering.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "geo": {"type": "string", "default": "NL"},
                "max_results": {"type": "integer", "minimum": 1, "maximum": 20, "default": 10},
                "query": {"type": "string"},
            },
            "additionalProperties": False,
        },
    },
    {
        "name": "google_trends_keyword_insights",
        "description": "Fetch Google Trends interest, related queries, related topics, and regional interest for a keyword.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "keyword": {"type": "string"},
                "geo": {"type": "string", "default": "NL"},
                "timeframe": {
                    "type": "string",
                    "default": "today 3-m",
                    "enum": ["now 7-d", "today 1-m", "today 3-m", "today 12-m", "today 5-y"],
                },
                "max_related": {"type": "integer", "minimum": 1, "maximum": 10, "default": 5},
                "max_points": {"type": "integer", "minimum": 3, "maximum": 20, "default": 8},
            },
            "required": ["keyword"],
            "additionalProperties": False,
        },
    },
    {
        "name": "reddit_find_subreddits",
        "description": "Find subreddits related to an audience, niche, or topic using public Reddit search.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "limit": {"type": "integer", "minimum": 1, "maximum": 10, "default": 5},
                "sort": {
                    "type": "string",
                    "enum": ["relevance", "activity"],
                    "default": "relevance",
                },
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "reddit_subreddit_details",
        "description": "Fetch subreddit metadata, posting guidance, and community rules using public Reddit endpoints.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "subreddit": {"type": "string"},
            },
            "required": ["subreddit"],
            "additionalProperties": False,
        },
    },
    {
        "name": "reddit_top_posts",
        "description": "Fetch top or feed-ranked posts from a subreddit over a selected timeframe.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "subreddit": {"type": "string"},
                "limit": {"type": "integer", "minimum": 1, "maximum": 10, "default": 5},
                "sort": {
                    "type": "string",
                    "enum": ["top", "hot", "new", "rising", "controversial"],
                    "default": "top",
                },
                "timeframe": {
                    "type": "string",
                    "enum": ["hour", "day", "week", "month", "year", "all"],
                    "default": "week",
                },
            },
            "required": ["subreddit"],
            "additionalProperties": False,
        },
    },
    {
        "name": "reddit_search_posts",
        "description": "Search posts inside a subreddit and return a ranked list of matching posts.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "subreddit": {"type": "string"},
                "query": {"type": "string"},
                "limit": {"type": "integer", "minimum": 1, "maximum": 10, "default": 5},
                "sort": {
                    "type": "string",
                    "enum": ["relevance", "top", "new", "comments"],
                    "default": "relevance",
                },
                "timeframe": {
                    "type": "string",
                    "enum": ["hour", "day", "week", "month", "year", "all"],
                    "default": "month",
                },
            },
            "required": ["subreddit", "query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "reddit_post_thread",
        "description": "Fetch a Reddit post and its top comments using a post URL or permalink.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "comment_limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 6},
                "comment_sort": {
                    "type": "string",
                    "enum": ["best", "top", "new", "controversial", "old", "qa"],
                    "default": "best",
                },
            },
            "required": ["url"],
            "additionalProperties": False,
        },
    },
]


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._skip = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip = True

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip = False
        elif tag in {"p", "div", "section", "article", "li", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip and data.strip():
            self.parts.append(data.strip())

    def get_text(self) -> str:
        text = " ".join(self.parts)
        text = re.sub(r"\s+\n", "\n", text)
        text = re.sub(r"\n\s+", "\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def read_message() -> dict[str, Any] | None:
    headers: dict[str, str] = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in {b"\r\n", b"\n"}:
            break
        key, _, value = line.decode("utf-8").partition(":")
        headers[key.strip().lower()] = value.strip()

    length = int(headers.get("content-length", "0"))
    if length <= 0:
        return None

    body = sys.stdin.buffer.read(length)
    if not body:
        return None
    return json.loads(body.decode("utf-8"))


def send_message(payload: dict[str, Any]) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\n\r\n".encode("utf-8")
    sys.stdout.buffer.write(header)
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


def send_response(message_id: Any, result: dict[str, Any]) -> None:
    send_message({"jsonrpc": "2.0", "id": message_id, "result": result})


def send_error(message_id: Any, code: int, message: str) -> None:
    send_message({"jsonrpc": "2.0", "id": message_id, "error": {"code": code, "message": message}})


def http_get(url: str, *, accept: str = "text/html,application/xhtml+xml", max_bytes: int = 1_000_000) -> tuple[str, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": DEFAULT_USER_AGENT,
            "Accept": accept,
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            content_type = response.headers.get("Content-Type", "")
            raw = response.read(max_bytes)
            return raw.decode("utf-8", errors="replace"), content_type
    except urllib.error.HTTPError:
        completed = subprocess.run(
            [
                "curl",
                "-L",
                "-sS",
                "-A",
                DEFAULT_USER_AGENT,
                "-H",
                f"Accept: {accept}",
                url,
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        return completed.stdout[:max_bytes], "text/html; charset=utf-8"


def curl_get(
    url: str,
    *,
    accept: str = "*/*",
    max_bytes: int = 1_000_000,
    cookie_jar: str | None = None,
    save_cookie_jar: str | None = None,
) -> str:
    command = [
        "curl",
        "-L",
        "-sS",
        "-A",
        DEFAULT_USER_AGENT,
        "-H",
        f"Accept: {accept}",
        "-H",
        "Accept-Language: en-US,en;q=0.9",
    ]
    if cookie_jar:
        command.extend(["-b", cookie_jar])
    if save_cookie_jar:
        command.extend(["-c", save_cookie_jar])
    command.append(url)
    completed = subprocess.run(command, capture_output=True, text=True, check=True)
    return completed.stdout[:max_bytes]


def google_trends_json(path: str, params: dict[str, Any], cookie_jar: str) -> dict[str, Any]:
    url = "https://trends.google.com" + path + "?" + urllib.parse.urlencode(params)
    last_error: RuntimeError | None = None
    for attempt in range(3):
        raw = curl_get(url, accept="application/json,text/javascript,*/*", cookie_jar=cookie_jar)
        trimmed = raw.lstrip()
        if trimmed.startswith("<"):
            if "429" in trimmed or "Too Many Requests" in trimmed:
                last_error = RuntimeError("Google Trends rate limited the request")
                time.sleep(0.75 * (attempt + 1))
                continue
            raise RuntimeError("Google Trends returned HTML instead of JSON")

        cleaned = raw[5:] if raw.startswith(")]}'") else raw
        return json.loads(cleaned)

    raise last_error or RuntimeError("Google Trends request failed")


def google_trends_ranked_items(payload: dict[str, Any], max_items: int) -> dict[str, list[dict[str, Any]]]:
    ranked_lists = payload.get("default", {}).get("rankedList", [])

    def normalize(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        for entry in entries[:max_items]:
            normalized = {key: entry.get(key) for key in ("query", "topic", "title", "value", "formattedValue", "link")}
            if not any(normalized.values()):
                normalized = entry
            items.append(normalized)
        return items

    result = {"top": [], "rising": []}
    if ranked_lists:
        result["top"] = normalize(ranked_lists[0].get("rankedKeyword", []))
    if len(ranked_lists) > 1:
        result["rising"] = normalize(ranked_lists[1].get("rankedKeyword", []))
    return result


def google_trends_interest_summary(points: list[dict[str, Any]], max_points: int) -> dict[str, Any]:
    values: list[int] = []
    simplified_points: list[dict[str, Any]] = []
    for point in points:
        raw_values = point.get("value") or []
        if not raw_values:
            continue
        score = int(raw_values[0])
        simplified_points.append(
            {
                "date": point.get("formattedTime") or point.get("time"),
                "axis_label": point.get("formattedAxisTime"),
                "score": score,
            }
        )
        values.append(score)

    if not values:
        return {"status": "no_data", "recent_points": []}

    peak_index = max(range(len(values)), key=values.__getitem__)
    peak = simplified_points[peak_index]

    window = min(4, len(values))
    recent_avg = sum(values[-window:]) / window
    previous_values = values[-2 * window : -window] if len(values) >= window * 2 else values[:-window]

    if previous_values:
        previous_avg = sum(previous_values) / len(previous_values)
        delta = recent_avg - previous_avg
        if delta >= 3:
            direction = "up"
        elif delta <= -3:
            direction = "down"
        else:
            direction = "flat"
    else:
        previous_avg = None
        direction = "flat"
        delta = None

    return {
        "status": "ok",
        "latest_score": values[-1],
        "average_score": round(sum(values) / len(values), 2),
        "peak": {"date": peak["date"], "score": peak["score"]},
        "recent_direction": direction,
        "recent_delta_points": None if delta is None else round(delta, 2),
        "recent_points": simplified_points[-max_points:],
    }


def google_trends_trending_searches(arguments: dict[str, Any]) -> str:
    geo = (str(arguments.get("geo", "NL")).strip() or "NL").upper()
    max_results = int(arguments.get("max_results", 10))
    query = str(arguments.get("query", "")).strip()
    query_tokens = re.findall(r"[a-z0-9]+", query.lower())

    rss_text = curl_get(f"https://trends.google.com/trending/rss?geo={urllib.parse.quote(geo)}", accept="application/rss+xml,application/xml,text/xml")
    root = ET.fromstring(rss_text)
    namespace = {"ht": "https://trends.google.com/trending/rss"}

    results: list[dict[str, Any]] = []
    for item in root.findall("./channel/item"):
        title = item.findtext("title", default="").strip()
        news_items = []
        for news_item in item.findall("ht:news_item", namespace):
            news_items.append(
                {
                    "title": news_item.findtext("ht:news_item_title", default="", namespaces=namespace).strip(),
                    "url": news_item.findtext("ht:news_item_url", default="", namespaces=namespace).strip(),
                    "source": news_item.findtext("ht:news_item_source", default="", namespaces=namespace).strip(),
                }
            )

        searchable = " ".join([title] + [news.get("title", "") for news in news_items] + [news.get("source", "") for news in news_items]).lower()
        searchable_tokens = set(re.findall(r"[a-z0-9]+", searchable))
        if query_tokens and not all(token in searchable_tokens for token in query_tokens):
            continue

        results.append(
            {
                "title": title,
                "approx_traffic": item.findtext("ht:approx_traffic", default="", namespaces=namespace).strip(),
                "published": item.findtext("pubDate", default="").strip(),
                "picture_source": item.findtext("ht:picture_source", default="", namespaces=namespace).strip(),
                "news": news_items[:3],
            }
        )
        if len(results) >= max_results:
            break

    return json.dumps(
        {
            "geo": geo,
            "query": query or None,
            "results": results,
        },
        indent=2,
        ensure_ascii=False,
    )


def google_trends_keyword_insights(arguments: dict[str, Any]) -> str:
    keyword = str(arguments["keyword"]).strip()
    geo = (str(arguments.get("geo", "NL")).strip() or "NL").upper()
    timeframe = str(arguments.get("timeframe", "today 3-m")).strip() or "today 3-m"
    max_related = int(arguments.get("max_related", 5))
    max_points = int(arguments.get("max_points", 8))
    warnings: list[str] = []

    with tempfile.NamedTemporaryFile() as cookie_jar:
        warm_url = f"https://trends.google.com/trends/explore/?geo={urllib.parse.quote(geo)}"
        curl_get(warm_url, save_cookie_jar=cookie_jar.name)

        explore_payload = {
            "comparisonItem": [{"keyword": keyword, "geo": geo, "time": timeframe}],
            "category": 0,
            "property": "",
        }
        params = {
            "hl": "en-US",
            "tz": "-120",
            "req": json.dumps(explore_payload, separators=(",", ":")),
        }
        explore = google_trends_json("/trends/api/explore", params, cookie_jar.name)

        widgets = {widget.get("id"): widget for widget in explore.get("widgets", [])}
        if not widgets:
            raise RuntimeError("Google Trends did not return any widgets")

        def widget_request(widget_id: str, endpoint: str) -> dict[str, Any]:
            widget = widgets.get(widget_id)
            if not widget:
                return {}
            widget_params = {
                "hl": "en-US",
                "tz": "-120",
                "req": json.dumps(widget.get("request", {}), separators=(",", ":")),
                "token": widget.get("token", ""),
            }
            try:
                payload = google_trends_json(endpoint, widget_params, cookie_jar.name)
                time.sleep(0.35)
                return payload
            except RuntimeError as exc:
                warnings.append(f"{widget_id}: {exc}")
                return {}

        timeseries = widget_request("TIMESERIES", "/trends/api/widgetdata/multiline")
        related_queries = widget_request("RELATED_QUERIES", "/trends/api/widgetdata/relatedsearches")
        related_topics = widget_request("RELATED_TOPICS", "/trends/api/widgetdata/relatedsearches")
        regions = widget_request("GEO_MAP", "/trends/api/widgetdata/comparedgeo")

    region_rows = []
    for row in regions.get("default", {}).get("geoMapData", []):
        values = row.get("value") or []
        if not values:
            continue
        region_rows.append(
            {
                "geo_code": row.get("geoCode"),
                "name": row.get("geoName"),
                "score": int(values[0]),
            }
        )
    region_rows.sort(key=lambda item: item["score"], reverse=True)

    return json.dumps(
        {
            "keyword": keyword,
            "geo": geo,
            "timeframe": timeframe,
            "interest_summary": google_trends_interest_summary(timeseries.get("default", {}).get("timelineData", []), max_points),
            "top_regions": region_rows[:max_related],
            "related_queries": google_trends_ranked_items(related_queries, max_related),
            "related_topics": google_trends_ranked_items(related_topics, max_related),
            "warnings": warnings or None,
        },
        indent=2,
        ensure_ascii=False,
    )


def web_search(arguments: dict[str, Any]) -> str:
    query = str(arguments["query"]).strip()
    max_results = int(arguments.get("max_results", 5))
    site = str(arguments.get("site", "")).strip()
    search_query = f"site:{site} {query}" if site else query
    url = "https://www.bing.com/search?format=rss&q=" + urllib.parse.quote(search_query)
    xml_text, _ = http_get(url, accept="application/rss+xml,application/xml,text/xml")

    root = ET.fromstring(xml_text)
    items = root.findall("./channel/item")
    results: list[dict[str, str]] = []
    for item in items[:max_results]:
        results.append(
            {
                "title": item.findtext("title", default="").strip(),
                "url": item.findtext("link", default="").strip(),
                "snippet": item.findtext("description", default="").strip(),
                "published": item.findtext("pubDate", default="").strip(),
            }
        )

    return json.dumps(
        {
            "query": query,
            "site": site or None,
            "results": results,
        },
        indent=2,
        ensure_ascii=False,
    )


def fetch_page(arguments: dict[str, Any]) -> str:
    url = str(arguments["url"]).strip()
    max_chars = int(arguments.get("max_chars", 12000))
    html, content_type = http_get(url)

    blocked_markers = ("Just a moment...", "Attention Required!", "cf-browser-verification")
    if any(marker in html for marker in blocked_markers):
        mirror_url = "https://r.jina.ai/" + url
        mirrored, _ = http_get(mirror_url, accept="text/plain,text/markdown,text/html")
        return json.dumps(
            {
                "url": url,
                "content_type": "text/markdown; charset=utf-8",
                "title": "",
                "text": mirrored[:max_chars],
            },
            indent=2,
            ensure_ascii=False,
        )

    if "html" not in content_type and not html.lstrip().startswith("<"):
        text = html[:max_chars]
        return json.dumps(
            {"url": url, "content_type": content_type, "text": text},
            indent=2,
            ensure_ascii=False,
        )

    title_match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    title = re.sub(r"\s+", " ", title_match.group(1)).strip() if title_match else ""
    parser = TextExtractor()
    parser.feed(html)
    text = parser.get_text()[:max_chars]

    return json.dumps(
        {
            "url": url,
            "content_type": content_type,
            "title": title,
            "text": text,
        },
        indent=2,
        ensure_ascii=False,
    )


def search_unsplash(arguments: dict[str, Any]) -> str:
    params = {
        "query": str(arguments["query"]).strip(),
        "per_page": str(int(arguments.get("per_page", 6))),
        "page": str(int(arguments.get("page", 1))),
    }
    orientation = arguments.get("orientation")
    if orientation:
        params["orientation"] = str(orientation)

    url = "https://unsplash.com/napi/search/photos?" + urllib.parse.urlencode(params)
    completed = subprocess.run(
        ["curl", "-sS", url],
        capture_output=True,
        text=True,
        check=True,
    )
    payload = json.loads(completed.stdout)
    items = []
    for result in payload.get("results", []):
        items.append(
            {
                "id": result.get("id"),
                "description": result.get("description") or result.get("alt_description") or "",
                "photo_page": result.get("links", {}).get("html"),
                "regular_url": result.get("urls", {}).get("regular"),
                "thumb_url": result.get("urls", {}).get("thumb"),
                "photographer": result.get("user", {}).get("name"),
                "photographer_profile": result.get("user", {}).get("links", {}).get("html"),
            }
        )

    return json.dumps(
        {
            "query": params["query"],
            "results": items,
        },
        indent=2,
        ensure_ascii=False,
    )


def normalize_subreddit_name(value: str) -> str:
    subreddit = value.strip()
    subreddit = re.sub(r"^https?://(?:old\.)?reddit\.com/r/", "", subreddit, flags=re.IGNORECASE)
    subreddit = subreddit.replace("/r/", "")
    subreddit = subreddit.strip("/")
    subreddit = re.sub(r"[^A-Za-z0-9_]+", "", subreddit)
    if not subreddit:
        raise ValueError("A subreddit name is required")
    return subreddit


def reddit_text(value: str | None) -> str:
    if not value:
        return ""
    unescaped = html.unescape(value)
    parser = TextExtractor()
    parser.feed(unescaped)
    text = parser.get_text()
    if text:
        return text
    return re.sub(r"\s+", " ", unescaped).strip()


def reddit_json(url: str) -> Any:
    payload, _ = http_get(url, accept="application/json,text/json,*/*")
    return json.loads(payload)


def reddit_listing_posts(payload: dict[str, Any], max_items: int) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    children = payload.get("data", {}).get("children", [])
    for child in children[:max_items]:
        data = child.get("data", {})
        items.append(
            {
                "subreddit": data.get("subreddit"),
                "title": data.get("title"),
                "author": data.get("author"),
                "score": data.get("score"),
                "num_comments": data.get("num_comments"),
                "created_utc": data.get("created_utc"),
                "upvote_ratio": data.get("upvote_ratio"),
                "is_self": data.get("is_self"),
                "post_hint": data.get("post_hint"),
                "link_flair_text": data.get("link_flair_text"),
                "domain": data.get("domain"),
                "url": data.get("url"),
                "permalink": "https://old.reddit.com" + data.get("permalink", ""),
                "selftext_excerpt": reddit_text(data.get("selftext"))[:400],
            }
        )
    return items


def reddit_comment_listing(payload: dict[str, Any], max_items: int) -> list[dict[str, Any]]:
    comments: list[dict[str, Any]] = []
    children = payload.get("data", {}).get("children", [])
    for child in children:
        if len(comments) >= max_items:
            break
        if child.get("kind") != "t1":
            continue
        data = child.get("data", {})
        replies = data.get("replies")
        reply_count = 0
        if isinstance(replies, dict):
            reply_count = len(replies.get("data", {}).get("children", []))
        comments.append(
            {
                "author": data.get("author"),
                "score": data.get("score"),
                "created_utc": data.get("created_utc"),
                "body": reddit_text(data.get("body"))[:800],
                "reply_count": reply_count,
                "permalink": "https://old.reddit.com" + data.get("permalink", ""),
            }
        )
    return comments


def reddit_find_subreddits(arguments: dict[str, Any]) -> str:
    query = str(arguments["query"]).strip()
    limit = int(arguments.get("limit", 5))
    sort = str(arguments.get("sort", "relevance")).strip() or "relevance"
    url = (
        "https://old.reddit.com/subreddits/search.json?"
        + urllib.parse.urlencode({"q": query, "limit": limit, "sort": sort})
    )
    payload = reddit_json(url)

    results = []
    for child in payload.get("data", {}).get("children", [])[:limit]:
        data = child.get("data", {})
        results.append(
            {
                "name": data.get("display_name"),
                "title": data.get("title"),
                "public_description": reddit_text(data.get("public_description")),
                "subscribers": data.get("subscribers"),
                "active_user_count": data.get("active_user_count"),
                "submission_type": data.get("submission_type"),
                "over18": data.get("over18"),
                "url": "https://old.reddit.com" + data.get("url", ""),
            }
        )

    return json.dumps(
        {"query": query, "sort": sort, "results": results},
        indent=2,
        ensure_ascii=False,
    )


def reddit_subreddit_details(arguments: dict[str, Any]) -> str:
    subreddit = normalize_subreddit_name(str(arguments["subreddit"]))
    about = reddit_json(f"https://old.reddit.com/r/{subreddit}/about.json")
    rules = reddit_json(f"https://old.reddit.com/r/{subreddit}/about/rules.json")
    data = about.get("data", {})
    result = {
        "subreddit": subreddit,
        "title": data.get("title"),
        "public_description": reddit_text(data.get("public_description")),
        "description": reddit_text(data.get("description")),
        "subscribers": data.get("subscribers"),
        "active_user_count": data.get("active_user_count"),
        "submission_type": data.get("submission_type"),
        "allow_images": data.get("allow_images"),
        "allow_videos": data.get("allow_videos"),
        "over18": data.get("over18"),
        "lang": data.get("lang"),
        "posting_guidance": reddit_text(data.get("submit_text_html")),
        "rules": [
            {
                "short_name": rule.get("short_name"),
                "description": reddit_text(rule.get("description")),
                "kind": rule.get("kind"),
                "violation_reason": rule.get("violation_reason"),
            }
            for rule in rules.get("rules", [])
        ],
        "url": f"https://old.reddit.com/r/{subreddit}/",
    }
    return json.dumps(result, indent=2, ensure_ascii=False)


def reddit_top_posts(arguments: dict[str, Any]) -> str:
    subreddit = normalize_subreddit_name(str(arguments["subreddit"]))
    limit = int(arguments.get("limit", 5))
    sort = str(arguments.get("sort", "top")).strip() or "top"
    timeframe = str(arguments.get("timeframe", "week")).strip() or "week"
    params = {"limit": limit}
    if sort in {"top", "controversial"}:
        params["t"] = timeframe
    url = f"https://old.reddit.com/r/{subreddit}/{sort}.json?" + urllib.parse.urlencode(params)
    payload = reddit_json(url)
    return json.dumps(
        {
            "subreddit": subreddit,
            "sort": sort,
            "timeframe": timeframe,
            "results": reddit_listing_posts(payload, limit),
        },
        indent=2,
        ensure_ascii=False,
    )


def reddit_search_posts(arguments: dict[str, Any]) -> str:
    subreddit = normalize_subreddit_name(str(arguments["subreddit"]))
    query = str(arguments["query"]).strip()
    limit = int(arguments.get("limit", 5))
    sort = str(arguments.get("sort", "relevance")).strip() or "relevance"
    timeframe = str(arguments.get("timeframe", "month")).strip() or "month"
    url = (
        f"https://old.reddit.com/r/{subreddit}/search.json?"
        + urllib.parse.urlencode(
            {
                "q": query,
                "restrict_sr": "1",
                "sort": sort,
                "t": timeframe,
                "limit": limit,
            }
        )
    )
    payload = reddit_json(url)
    return json.dumps(
        {
            "subreddit": subreddit,
            "query": query,
            "sort": sort,
            "timeframe": timeframe,
            "results": reddit_listing_posts(payload, limit),
        },
        indent=2,
        ensure_ascii=False,
    )


def reddit_post_thread(arguments: dict[str, Any]) -> str:
    url = str(arguments["url"]).strip()
    comment_limit = int(arguments.get("comment_limit", 6))
    comment_sort = str(arguments.get("comment_sort", "best")).strip() or "best"
    normalized = url
    if normalized.startswith("/"):
        normalized = "https://old.reddit.com" + normalized
    normalized = re.sub(r"^https?://(?:www\.)?reddit\.com", "https://old.reddit.com", normalized)
    normalized = normalized.rstrip("/")
    if not normalized.endswith(".json"):
        normalized += ".json"
    separator = "&" if "?" in normalized else "?"
    payload = reddit_json(
        normalized + separator + urllib.parse.urlencode({"limit": comment_limit, "sort": comment_sort}),
    )
    if not isinstance(payload, list) or len(payload) < 2:
        raise ValueError("Reddit thread response did not contain post and comment listings")

    post_listing = payload[0]
    comment_listing = payload[1]
    posts = reddit_listing_posts(post_listing, 1)
    if not posts:
        raise ValueError("Reddit thread response did not include a post")

    result = {
        "post": posts[0],
        "comments": reddit_comment_listing(comment_listing, comment_limit),
        "comment_sort": comment_sort,
    }
    return json.dumps(result, indent=2, ensure_ascii=False)


def call_tool(name: str, arguments: dict[str, Any]) -> str:
    if name == "web_search":
        return web_search(arguments)
    if name == "fetch_page":
        return fetch_page(arguments)
    if name == "search_unsplash":
        return search_unsplash(arguments)
    if name == "google_trends_trending_searches":
        return google_trends_trending_searches(arguments)
    if name == "google_trends_keyword_insights":
        return google_trends_keyword_insights(arguments)
    if name == "reddit_find_subreddits":
        return reddit_find_subreddits(arguments)
    if name == "reddit_subreddit_details":
        return reddit_subreddit_details(arguments)
    if name == "reddit_top_posts":
        return reddit_top_posts(arguments)
    if name == "reddit_search_posts":
        return reddit_search_posts(arguments)
    if name == "reddit_post_thread":
        return reddit_post_thread(arguments)
    raise ValueError(f"Unknown tool: {name}")


def main() -> int:
    while True:
        message = read_message()
        if message is None:
            return 0

        message_id = message.get("id")
        method = message.get("method")

        try:
            if method == "initialize":
                send_response(
                    message_id,
                    {
                        "protocolVersion": PROTOCOL_VERSION,
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                    },
                )
            elif method == "notifications/initialized":
                continue
            elif method == "ping":
                send_response(message_id, {})
            elif method == "tools/list":
                send_response(message_id, {"tools": TOOLS})
            elif method == "tools/call":
                params = message.get("params", {})
                name = params.get("name")
                arguments = params.get("arguments", {})
                text = call_tool(str(name), dict(arguments))
                send_response(message_id, {"content": [{"type": "text", "text": text}], "isError": False})
            else:
                send_error(message_id, -32601, f"Method not found: {method}")
        except Exception as exc:  # pragma: no cover
            details = "".join(traceback.format_exception_only(type(exc), exc)).strip()
            send_error(message_id, -32000, details)


if __name__ == "__main__":
    sys.exit(main())
