{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "97990c3b-b250-4971-92ed-e42bd21ab02e",
      "cell_type": "code",
      "source": "import streamlit as st\nimport pandas as pd\nimport plotly.express as px\n\n\n@st.cache_data\ndef load_data():\n    return pd.read_csv('cleaned_student_data.csv')\n\ndf = load_data()\n\n\nst.title(\"📊 Student Mathematics Performance\")\nst.write(\"Interactive Dashboard for Educational Data Analysis\")\n\n\nst.sidebar.header(\"Filter Data\")\n\n\nstudy_time = st.sidebar.selectbox(\n    \"Select Weekly Study Time\",\n    [\"All\", \"1 (<2 hours)\", \"2 (2-5 hours)\", \"3 (5-10 hours)\", \"4 (>10 hours)\"]\n)\n\nif study_time != \"All\":\n   \n    category_num = int(study_time[0])\n    filtered_df = df[df[\"studytime\"] == category_num]\nelse:\n    filtered_df = df\n\nst.subheader(\"📊 Summary Statistics\")\ncol1, col2, col3 = st.columns(3)\n\ncol1.metric(\"Number of Students\", len(filtered_df))\ncol2.metric(\"Average Final Grade\", round(filtered_df[\"G3\"].mean(), 2))\ncol3.metric(\"Highest Final Grade\", filtered_df[\"G3\"].max())\n\nst.subheader(\"📊 Performance Visualizations\")\n\nchart_col1, chart_col2 = st.columns(2)\n\nwith chart_col1:\n    fig1 = px.histogram(\n        filtered_df, \n        x=\"G3\", \n        nbins=20,\n        title=\"Final Grade (G3) Distribution\",\n        color_discrete_sequence=['#3498db']\n    )\n    st.plotly_chart(fig1, use_container_width=True)\n\nwith chart_col2:\n    fig2 = px.scatter(\n        filtered_df, \n        x=\"absences\", \n        y=\"G3\", \n        color=\"sex\",\n        title=\"Student Absences vs Final Grade\",\n        color_discrete_map={'female': '#e74c3c', 'male': '#2ecc71'}\n    )\n    st.plotly_chart(fig2, use_container_width=True)\n\nst.subheader(\"Filtered Dataset\")\nst.dataframe(filtered_df)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "ename": "<class 'ModuleNotFoundError'>",
          "evalue": "No module named 'streamlit'",
          "traceback": [
            "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
            "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
            "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mstreamlit\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mst\u001b[39;00m\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpd\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mplotly\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mexpress\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpx\u001b[39;00m\n",
            "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'streamlit'"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "60acc7f7-d679-4462-beb2-458af954ac2f",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}