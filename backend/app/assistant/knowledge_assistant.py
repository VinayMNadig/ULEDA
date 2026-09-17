from app.llm.llm import llm


def answer(question: str):

    prompt = f"""
You are ULEDA (Universal LLM Database Assistant).

The user is NOT asking to execute SQL.

Answer naturally like ChatGPT.

Rules:
- Do NOT generate SQL.
- Explain clearly.
- Use examples if needed.
- Keep answers concise.
- Be friendly.

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip()