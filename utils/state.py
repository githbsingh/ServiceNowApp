from typing import TypedDict
import pandas as pd

class AgentState(TypedDict):

    question: str
    dataframe: pd.DataFrame
    result: dict
    answer: str
    chart: object | None
    trace: list[str]
    schema: dict[str, object]
    