from app.llm.llm import llm


def generate_answer(question: str, sql: str, results):

    prompt = f"""
You are an AI Database Assistant.

User Question:
{question}

Generated SQL:
{sql}

Database Results:
{results}

Explain the answer in simple English.

If there are no records, politely say no data was found.

Do not mention SQL unless the user specifically asks for it.
"""

    response = llm.invoke(prompt)

    return response.content.strip()