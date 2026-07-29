import os
import pandas as pd
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# 1. CSV Data Load Karein
df = pd.read_csv("data/up-police-priority-data.csv")

def get_agent_response(query):
    # 2. Key Fetching with Verification
    api_key = ""
    
    # Check Streamlit Secrets
    if "OPENROUTER_API_KEY" in st.secrets:
        api_key = str(st.secrets["OPENROUTER_API_KEY"]).strip()
    
    # Backup Check Environment Variables
    if not api_key:
        api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()

    # Agar Key nahi mili toh UI par saaf message dikhayega
    if not api_key or len(api_key) < 10:
        return "⚠️ API Key Nahi Mili! Streamlit Settings > Secrets mein 'OPENROUTER_API_KEY' sahi se save karein."

    # OpenRouter Environment Variables Set Karein
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

    try:
        # 3. Hermes / Llama LLM Setup (OpenRouter Free Endpoint)
        llm = ChatOpenAI(
            model="meta-llama/llama-3.1-8b-instruct:free",
            openai_api_key=api_key,
            openai_api_base="https://openrouter.ai/api/v1",
            temperature=0.1,
            default_headers={
                "HTTP-Referer": "https://streamlit.io",
                "X-Title": "UP Police Analytics"
            }
        )

        # 4. Agent Execution
        agent = create_pandas_dataframe_agent(
            llm, 
            df, 
            verbose=True, 
            allow_dangerous_code=True
        )

        return agent.run(query)

    except Exception as e:
        return f"Data analyze karne mein error aaya: {str(e)}"
