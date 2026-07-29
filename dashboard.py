import streamlit as st
import pandas as pd
from agent import get_agent_response

st.set_page_config(
    page_title="UP Police Priority Analytics",
    page_icon="🚔",
    layout="wide"
)

st.title("🚔 UP Police Priority Analytics Dashboard")
st.write("Hermes / Llama LLM Agent dwara sanchalit Data Analytics System")

# Sidebar - Key Status Check
st.sidebar.header("🔑 API Key Status")
api_key_check = st.secrets.get("OPENROUTER_API_KEY", "")

if api_key_check:
    st.sidebar.success(f"✅ Key Found: {api_key_check[:6]}...{api_key_check[-4:]}")
else:
    st.sidebar.error("❌ Key NOT found in Secrets!")

# Dataset Overview
st.subheader("📊 Dataset Overview")
try:
    df = pd.read_csv("data/up-police-priority-data.csv")
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"Data load karne mein dikkat aayi: {e}")

st.markdown("---")

# Query Section
st.subheader("🤖 Data Agent se Sawaal Puchiye")
user_query = st.text_input("Apna sawaal yahan type karein:", placeholder="Jaise: Top 3 districts jahan sabse zyada police units deploy hain?")

if st.button("Analyze Data 🔍"):
    if user_query.strip():
        with st.spinner("Agent data ko analyze kar raha hai..."):
            response = get_agent_response(user_query)
            st.success("### Analysis Result:")
            st.write(response)
    else:
        st.warning("Kripya pehle koi sawaal type karein!")
