import pandas as pd

from models.llm import llm


def response_agent(state):
    """
    Response Agent

    Responsibilities:
    -----------------
    1. Convert analytics output into a natural language response.
    2. Preserve raw results for visualization.
    """

    question = state["question"]
    result = state["result"]

    # Convert different result types to text
    if isinstance(result, pd.DataFrame):
        result_text = result.head(20).to_markdown(index=False)

    elif isinstance(result, pd.Series):
        result_text = result.to_markdown()

    else:
        result_text = str(result)

    prompt = f"""
You are an expert ServiceNow Incident Analyst.

A user asked:

{question}

The analytics engine returned:

{result_text}

Instructions:

1. Answer ONLY using the analytics result.
2. Be concise and professional.
3. If the result is a table, summarize the important findings.
4. Do not invent information.
5. If the result is empty, politely tell the user that no matching records were found.
"""

    response = llm.invoke(prompt)
    print("💬 Response Agent: Response generated.")
    print(response.content)

    state["answer"] = response.content

    state.setdefault("trace", []).append(
        "💬 Response Agent: Response generated."
    )

    return state