import streamlit as st
import pandas as pd

from graph.workflow import graph


st.set_page_config(
    page_title="ServiceNow Incident AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 ServiceNow Incident Analytics")
st.caption("AI-powered Incident Analysis using LangGraph")


# ---------------------------------------------------
# Load CSV
# ---------------------------------------------------

csv_file = st.file_uploader(
    "Upload ServiceNow Incident CSV",
    type="csv"
)

if csv_file is None:
    st.info("Please upload a CSV file.")
    st.stop()


df = pd.read_csv(csv_file)

st.success(f"Loaded {len(df):,} incidents")


# Preview

with st.expander("Preview Data"):

    st.dataframe(
        df.head(),
        use_container_width=True
    )


# ---------------------------------------------------
# User Question
# ---------------------------------------------------

question = st.text_input(
    "Ask a question",
    placeholder="Example: Show top 10 assignment groups"
)


if st.button("Analyze"):

    if question.strip() == "":

        st.warning("Please enter a question.")

        st.stop()

    with st.spinner("Running AI Agents..."):

        result = graph.invoke(
                {
                    "question": question,
                    "dataframe": df,
                    "schema": {
                        "columns": df.columns.tolist(),
                        "dtypes": df.dtypes.astype(str).to_dict(),
                        "row_count": len(df)
                    },
                    "trace": []
                }
            )

    st.divider()

    st.subheader("💬 AI Answer")

    st.write(result["answer"])


    if isinstance(result["result"], pd.DataFrame):

        st.subheader("Returned Data")

        st.dataframe(
            result["result"],
            use_container_width=True
        )

    elif isinstance(result["result"], pd.Series):

        st.subheader("Returned Data")

        st.dataframe(
            result["result"].to_frame(),
            use_container_width=True
        )

    else:

        st.metric(
            "Result",
            result["result"]
        )


    if result.get("trace"):

        with st.expander("Agent Execution"):

            for step in result["trace"]:

                st.success(step)