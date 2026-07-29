import streamlit as st
import pandas as pd
from agent import get_agent_response

# Page configuration
st.set_page_config(
    page_title="UP Police Priority Analytics",
    page_icon="🚔",
    layout="wide"
)

# Header Section
st.title("🚔 UP Police Priority Analytics Dashboard")
st.write("Hermes LLM Agent dwara sanchalit Data Analytics System")

# Sidebar - Project Info
st.sidebar.header("📌 Project Details")
st.sidebar.info(
    "Yeh dashboard UP Police ke priority cases, response time, "
    "aur resource allocation ko analyze karne ke liye Hermes Agent ka upyog karta hai."
)

# 1. Dataset Preview Section
st.subheader("📊 Dataset Overview")
try:
    df = pd.read_csv("data/up-police-priority-data.csv")
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"Data load karne mein dikkat aayi: {e}")

st.markdown("---")

# 2. Interactive AI Agent Section
st.subheader("🤖 Hermes Data Agent se Sawaal Puchiye")
st.write("Aap natural language mein data ke baare mein koi bhi sawaal puch sakte hain.")

# Input Box
user_query = st.text_input(
    "Apna sawaal yahan type karein:",
    placeholder="Jaise: Kis district mein sabse zyada Critical cases hain?"
)

# Action Button
if st.button("Analyze Data 🔍"):
    if user_query.strip():
        with st.spinner("Hermes Agent data ko analyze kar raha hai..."):
            response = get_agent_response(user_query)
            st.success("### Analysis Result:")
            st.write(response)
    else:
        st.warning("Kripya pehle koi sawaal type karein!")

# Sample Questions for Workshop Demo
st.markdown("---")
with st.expander("💡 Workshop Presentation ke liye Sample Questions"):
    st.markdown("""
    - *"Kis district mein Critical priority cases sabse zyada hain?"*
    - *"Cyber Fraud ke kitne cases In Progress status mein hain?"*
    - *"Har district ka average response time kitna hai?"*
    - *"Top 3 districts jahan sabse zyada police units deploy hain?"*
    """)
