from tavily import TavilyClient
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# 🔎 SEARCH
def web_search(query: str):
    res = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=5  # 🔥 increase results
    )

    output = []

    for i, r in enumerate(res["results"], 1):
        output.append({
            "title": r.get("title", ""),
            "url": r.get("url", ""),
            "content": r.get("content", "")[:500],  # 🔥 longer context
            "score": r.get("score", ""),  # relevance score
        })

    return output


# 🌐 SCRAPE
def scrape_url(url: str):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "lxml")

        text = " ".join([p.get_text() for p in soup.find_all("p")])
        return text[:3000]

    except Exception as e:
        return f"Error: {str(e)}"