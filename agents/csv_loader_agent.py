from functools import lru_cache
from pathlib import Path
import pandas as pd

@lru_cache(maxsize=1)
def load_dataframe():
    csv_path = Path("data/incidents.csv")

    if not csv_path.exists():
        raise FileNotFoundError(f"{csv_path} not found.")

    return pd.read_csv(csv_path)


def csv_loader_agent(state):
    df = load_dataframe()

    state["dataframe"] = df

    state.setdefault("trace", []).append(
        f"📄 Loaded {len(df)} incidents."
    )

    return state