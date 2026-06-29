import code

import pandas as pd

from models.llm import llm


def analytics_agent(state):
    """
    Analytics Agent

    Responsibilities:
    -----------------
    1. Understand the user's question.
    2. Generate a Pandas query using Gemini.
    3. Execute the query.
    4. Store the result in graph state.
    """

    question = state["question"]
    df = state["dataframe"]

    columns = ", ".join(df.columns.tolist())
    print(f"Columns: {columns}")
    schema = state["schema"]

    prompt = f"""
You are an expert Python Pandas developer.

The dataframe is named df.

Columns are:

{columns}

Generate ONLY ONE valid Python Pandas expression.

The dataframe is named df.

Columns available:

incident_id
priority
category
subcategory
opened_by
description
impact
urgency
state

Column Values

state:
Open
Closed
Resolved

priority:
P1
P2
P3

category:
Network
Software

IMPORTANT:
- Column names are case-insensitive.
- Convert all column names to lowercase before using them.
- Never invent new columns.
- Use ONLY the columns listed above.

Rules:
1. Use ONLY the listed columns.
2. Never invent column names.
3. Return executable pandas code only.
4. If the requested column doesn't exist, return:
   COLUMN_NOT_FOUND:<column_name>

Examples:

Question:
How many open incidents?

Answer:
result = df[df["state"]=="Open"].shape[0]

Question:
Show P1 incidents.

Answer:
result = df[df["priority"]=="P1"]

Question:
Top 5 Assignment Groups

Answer:
result = df["Assignment Group"].value_counts().head(5)

Now answer:

{question}
"""

    response = llm.invoke(prompt)

    code = response.content.strip()
    print("="*80)
    print(code)
    print("="*80)

    local_scope = {
        "df": df
    }

    try:

        exec(code, {}, local_scope)
        
        print("COLUMNS:")
        print(df.columns.tolist())

        result = local_scope["result"]
        print("RESULT:")
        print(result)

    except Exception as e:

        result = f"Execution Failed: {str(e)}"

    state["result"] = result

    state.setdefault("trace", []).append(
        "📊 Analytics Agent: Query executed."
    )

    return state