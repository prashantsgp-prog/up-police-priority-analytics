import os
import pandas as pd
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# 1. Streamlit Secrets se API key read karein (Secure Way)
if "OPENROUTER_API_KEY" in st.secrets:
    api_key = st.secrets["OPENROUTER_API_KEY"]
else:
    api_key = os.environ.get("OPENROUTER_API_KEY", "")

# 2. Data load karein
df = pd.read_csv("data/up-police-priority-data.csv")

# 3. Hermes LLM Setup
llm = ChatOpenAI(
    model="nousresearch/nous-hermes-2-mixtral-8x7b-dpo",
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.1
)

# 4. Data Agent setup
agent = create_pandas_dataframe_agent(
    llm, 
    df, 
    verbose=True, 
    allow_dangerous_code=True
)

def get_agent_response(query):
    try:
        response = agent.run(query)
        return response
    except Exception as e:
        return f"Data analyze karne mein error aaya: {e}"
