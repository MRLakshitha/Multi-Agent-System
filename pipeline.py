from tools import web_search, scrape_url
from agents import writer_chain, critic_chain


def run_research_pipeline(topic: str):

    # =========================
    # STEP 1: SEARCH
    # =========================
    print("\n" + "="*50)
    print("STEP 1: SEARCH")
    print("="*50)

    results = web_search(topic)

    if not results:
        print("❌ No search results found")
        return

    urls = [r["url"] for r in results[:5]]

    # Print detailed search results
    for i, r in enumerate(results[:5], 1):
        print(f"\nResult {i}")
        print("Title :", r["title"])
        print("URL   :", r["url"])
        print("Snippet :", r["content"])
        print("-" * 50)

    # =========================
    # STEP 2: SCRAPE
    # =========================
    print("\n" + "="*50)
    print("STEP 2: SCRAPING")
    print("="*50)

    all_content = ""

    for url in urls:
        print(f"🔎 Scraping: {url}")
        content = scrape_url(url)

        all_content += f"\n\nSource: {url}\n{content[:1200]}"

    print("\n✅ Scraping completed")

    # =========================
    # STEP 3: PREPARE RESEARCH DATA
    # =========================
    print("\n" + "="*50)
    print("STEP 3: PREPARING DATA")
    print("="*50)

    search_text = ""

    for r in results[:5]:
        search_text += f"""
Title: {r['title']}
URL: {r['url']}
Snippet: {r['content']}
"""

    research = f"""
Topic: {topic}

=== SEARCH INSIGHTS ===
{search_text}

=== SCRAPED CONTENT ===
{all_content}

=== SOURCES ===
{chr(10).join(urls)}
"""

    # =========================
    # STEP 4: WRITE REPORT
    # =========================
    print("\n" + "="*50)
    print("STEP 4: WRITING REPORT")
    print("="*50)

    report = writer_chain.invoke({
        "topic": topic,
        "research": research
    })

    print("\n📄 FINAL REPORT:\n")
    print(report)

    # =========================
    # STEP 5: CRITIC
    # =========================
    print("\n" + "="*50)
    print("STEP 5: CRITIC REVIEW")
    print("="*50)

    feedback = critic_chain.invoke({
        "report": report
    })

    print("\n🧠 CRITIC FEEDBACK:\n")
    print(feedback)


# =========================
# MAIN ENTRY
# =========================
if __name__ == "__main__":
    print("🚀 Research System Started\n")
    topic = input("Enter research topic: ")
    run_research_pipeline(topic)