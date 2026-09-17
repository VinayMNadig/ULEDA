from app.llm.llm import llm


def explain_table_llm(table_name, columns, sample_rows, foreign_keys=None):
    """
    Asks the LLM for a short, warm, plain-English explanation of what
    a table is for, based on its real columns and a few real sample rows.
    """

    column_lines = "\n".join(
        f"  - {c['name']} ({c['type']})"
        for c in columns
    )

    fk_lines = ""

    if foreign_keys:
        fk_lines = "\n".join(
            f"  - {fk['column']} links to {fk['reference_table']}({fk['reference_column']})"
            for fk in foreign_keys
        )

    prompt = f"""
You are a friendly database assistant explaining a table to a non-technical
person. Be warm and conversational, like you're showing a friend around,
not writing documentation.

Table name: {table_name}

Columns:
{column_lines}

{"Relationships:" if fk_lines else ""}
{fk_lines}

Sample rows (real data from this table):
{sample_rows}

Write a short explanation (3-5 sentences) that:
1. Says in plain language what real-world thing this table stores
   (e.g. "This is where artist information lives").
2. Mentions 2-3 of the most meaningful columns and what they mean.
3. Gives ONE natural example of something the person could do with it
   (e.g. "you could add a new artist here" or "ask me to show all artists
   from a specific genre").

Do not use markdown headers or bullet lists. Write it as friendly prose.
Do not just repeat the raw column names mechanically.
"""

    response = llm.invoke(prompt)

    return response.content.strip()
