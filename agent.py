import os
import pandas as pd
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# 1. Streamlit Secrets se Key Read karein
api_key = ""
if "OPENROUTER_API_KEY" in st.secrets:
    api_key = st.secrets["OPENROUTER_API_KEY"]
else:
    api_key = os.environ.get("OPENROUTER_API_KEY", "")

# 2. Data File Load karein
df = pd.read_csv("data/up-police-priority-data.csv")

# 3. Hermes LLM Setup (OpenRouter Required Headers ke saath)
llm = ChatOpenAI(
    model="nousresearch/nous-hermes-2-mixtral-8x7b-dpo:free",  # :free tag lagaya hai taaki zero balance par bhi chale
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://streamlit.io",
        "X-Title": "UP Police Analytics"
    },
    temperature=0.1
)

# 4. Agent Initialization
agent = create_pandas_dataframe_agent(
    llm, 
    df, 
    verbose=True, 
    allow_dangerous_code=True
)

def get_agent_response(query):
    if not api_key:
        return "⚠️ Error: Streamlit Secrets mein API Key nahi mili. Kripya Settings > Secrets check karein."
    try:
        response = agent.run(query)
        return response
    except Exception as e:
        return f"Data analyze karne mein error aaya: {e}"
