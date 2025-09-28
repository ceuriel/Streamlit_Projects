import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from numpy.random import default_rng as rng

df = pd.read_csv("state_data.csv")

st.header("Changes in US State Demographics Over Time")

# Let user select which state to graph
state = st.selectbox("State:", df["State"].unique())

# Let user select which Demographics to graph
demographics = st.selectbox("Demographics:", ["Total Population", "Median Household Income"])


# Create tabs for graph and table
graph_tab, table_tab = st.tabs(["📈 Graphs", "🔍 Table"])

with graph_tab:
    # Create the graph the user requested
    df_state = df[df["State"] == state]
    if demographics == "Total Population":
        fig = px.line(
            df_state,
            x="Year",
            y="Total Population",
            title=f"Total Population of {state}",
        )
    elif demographics == "Median Household Income":
        fig = px.line(
            df_state,
            x="Year",
            y="Median Household Income",
            title=f"Median Household Income of {state}",
        )
    else:
        raise ValueError("Unknown demographics!")
    st.plotly_chart(fig)
with table_tab:
    # Render the entire dataframe
    st.dataframe(df)