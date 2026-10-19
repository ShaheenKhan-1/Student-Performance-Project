import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    # Make sure this path points to where your CSV is saved
    return pd.read_csv('Data/cleaned_student_data.csv')

df = load_data()

st.title("📊 Student Mathematics Performance")
st.write("Interactive Dashboard for Educational Data Analysis")

st.sidebar.header("Filter Data")

study_time = st.sidebar.selectbox(
    "Select Weekly Study Time",
    ["All", "1 (<2 hours)", "2 (2-5 hours)", "3 (5-10 hours)", "4 (>10 hours)"]
)

if study_time != "All":
    category_num = int(study_time[0])
    filtered_df = df[df["studytime"] == category_num]
else:
    filtered_df = df

st.subheader("📊 Summary Statistics")
col1, col2, col3 = st.columns(3)

col1.metric("Number of Students", len(filtered_df))
col2.metric("Average Final Grade", round(filtered_df["G3"].mean(), 2))
col3.metric("Highest Final Grade", filtered_df["G3"].max())

st.subheader("📊 Performance Visualizations")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    fig1 = px.histogram(
        filtered_df, 
        x="G3", 
        nbins=20,
        title="Final Grade (G3) Distribution",
        color_discrete_sequence=['#3498db']
    )
    st.plotly_chart(fig1, use_container_width=True)

with chart_col2:
    fig2 = px.scatter(
        filtered_df, 
        x="absences", 
        y="G3", 
        color="sex",
        title="Student Absences vs Final Grade",
        color_discrete_map={'female': '#e74c3c', 'male': '#2ecc71'}
    )
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Filtered Dataset")
st.dataframe(filtered_df)