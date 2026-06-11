import streamlit as st
import pandas as pd


def load_data() -> pd.DataFrame:
    """Load or generate data for the app."""
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana"],
        "Score": [85, 92, 78, 88],
        "Department": ["HR", "IT", "Finance", "Marketing"],
    }
    return pd.DataFrame(data)


def render_sidebar() -> dict:
    """Render sidebar controls and return selected options."""
    st.sidebar.title("Controls")
    department = st.sidebar.selectbox(
        "Select Department",
        ["All", "HR", "IT", "Finance", "Marketing"],
    )
    show_raw = st.sidebar.checkbox("Show raw data", value=False)
    return {"department": department, "show_raw": show_raw}


def filter_data(df: pd.DataFrame, department: str) -> pd.DataFrame:
    """Filter the DataFrame by department."""
    if department == "All":
        return df
    return df[df["Department"] == department]


def main() -> None:
    st.set_page_config(page_title="Streamlit Boilerplate", layout="wide")

    st.title("Streamlit Application Boilerplate")
    st.markdown(
        "This is a starter Streamlit app with a sidebar filter, data table, and summary stats."
    )

    df = load_data()
    options = render_sidebar()

    filtered_df = filter_data(df, options["department"])

    st.header("Summary")
    st.metric("Total rows", len(filtered_df))
    st.metric("Average score", f"{filtered_df['Score'].mean():.1f}")

    st.header("Data Preview")
    st.dataframe(filtered_df)

    if options["show_raw"]:
        st.header("Raw Data")
        st.write(df)


if __name__ == "__main__":
    main()
