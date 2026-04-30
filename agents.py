from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# ✍ WRITER
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional research writer."),
    ("human", """
Write a detailed research report.

Topic: {topic}

Research Data:
{research}

IMPORTANT:
- Use ONLY given URLs
- Do NOT make up sources

Structure:
- Introduction
- Key Findings (min 3)
- Conclusion
- Sources (URLs only)
""")
])

writer_chain = writer_prompt | llm | StrOutputParser()


# 🔍 CRITIC
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict critic."),
    ("human", """
Review this report:

{report}

Give:
Score: X/10

Strengths:
- ...

Weaknesses:
- ...

Verdict:
...
""")
])

critic_chain = critic_prompt | llm | StrOutputParser()