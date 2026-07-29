import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# 1. Yahan apni actual API Key quotes "" ke andar paste karein
MY_API_KEY = "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"

# 2. Data file load karein
df = pd.read_csv("data/up-police-priority-data.csv")

# 3. Hermes LLM Model initialize karein
llm = ChatOpenAI(
    model="nousresearch/nous-hermes-2-mixtral-8x7b-dpo",
    openai_api_key=MY_API_KEY,
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
