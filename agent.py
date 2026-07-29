[4:34 pm, 29/7/2026] PRASHANT SINGH: tabulate
[4:38 pm, 29/7/2026] PRASHANT SINGH: import pandas as pd
import os
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Yahan apni actual API Key paste karein
MY_API_KEY = "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"

df = pd.read_csv("data/up-police-priority-data.csv")

# Hermes Model Setup with explicit API Key
llm = ChatOpenAI(
    model="nousresearch/nous-hermes-2-mixtral-8x7b-dpo",
    openai_api_key=MY_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.1
)

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
