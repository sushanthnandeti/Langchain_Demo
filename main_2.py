from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_MODEL   = "gpt-3.5-turbo"
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

def main():
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name=OPENAI_MODEL,
    )
    chain_new = APIChain.from_llm_and_api_docs(
        llm,
        open_meteo_docs.OPEN_METEO_DOCS,
        limit_to_domains=["https://api.open-meteo.com"],
        verbose=False,
    )
    result = chain_new.invoke(  # .run is deprecated
        "What is the weather right now in Jersey City, New Jersey, USA in Celsius?"
    )
    print(result)

if __name__ == "__main__":
    main()