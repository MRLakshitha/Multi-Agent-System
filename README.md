AI-powered research system that performs real-time web search, scraping, report generation, and critique using multi-agent architecture.
Overview

This project is a multi-agent AI research pipeline that mimics how humans perform research:

Search for information
Read articles
Extract insights
Write structured report
Critically evaluate output

It combines:

🌐 Web search (Tavily)
🧠 LLM reasoning (Groq LLaMA)
📄 Web scraping (BeautifulSoup)
🔁 Pipeline orchestration

Architecture:

Tech Stack:

Category        	Technology
Language         	Python
LLM              	Groq (LLaMA 3.1)
Framework         LangChain (LCEL)
Search            API	Tavily
Scraping	        BeautifulSoup
HTTP	            Requests
Env	              python-dotenv

Project Structure
multi-agent-system/
│── agents.py        # Writer & Critic agents
│── tools.py         # Search + Scraping tools
│── pipeline.py      # Main orchestration
│── .env             # API keys
│── requirements.txt
│── README.md

How It Works
🔎 Step 1: Search
Uses Tavily API
Retrieves top results with URLs + snippets
🌐 Step 2: Scraping
Extracts real content from webpages
Uses BeautifulSoup
🧠 Step 3: Report Generation
LLM generates structured research report
🔍 Step 4: Critic Review
LLM evaluates report quality

installation:
git clone https://github.com/your-username/multi-agent-system.git
cd multi-agent-system

python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
Environment Variables

Create .env file:

TAVILY_API_KEY=your_key
GROQ_API_KEY=your_key
Run
python pipeline.py

Features
🔍 Real-time web search
🌐 Multi-page scraping
🧠 AI-generated reports
🔍 AI-based critique
📊 Structured output
💰 Fully free LLM support

Limitations
Some websites block scraping
No ranking/filtering yet
Sequential (not parallel)
CLI-based (no UI)
