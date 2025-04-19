import os 
from  dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
load_dotenv()

OPENAI_MODEL = 'gpt-4'
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def main():
    llm = ChatOpenAI(openai_api_key = OPENAI_API_KEY, model_name = OPENAI_MODEL)
    result = llm.predict(" Who are the highest selling rappers of all time. Give the ranking from highest to lowest")
    print(result)

if __name__ == "__main__": 
    main()