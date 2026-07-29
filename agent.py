import pandas as pd
import os
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# 1. Apni Hermes / OpenRouter API Key yahan paste karein
os.environ["OPENAI_API_KEY"] = "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"

# 2. CSV Data Load karein
df = pd.read_csv("data/up-police-priority-data.csv")

# 3. Hermes LLM Setup
# Note: Agar aap OpenRouter use kar rahe hain toh base_url OpenRouter ka rahega
llm = ChatOpenAI(
    model="nousresearch/nous-hermes-2-mixtral-8x7b-dpo", # Ya jo Hermes model aap use kar rahe ho
    openai_api_base="https://openrouter.ai/api/v1",       # Agar OpenRouter key hai toh yeh rehne dein
    temperature=0.1
)

# 4. Data Analytics Agent create karein
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
