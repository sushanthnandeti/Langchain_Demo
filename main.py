import os 
from  dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser


class Country(BaseModel):
    capital: str = Field(description = "Capital of the Country")
    name: str = Field(description="Name of the Country")

load_dotenv()

OPENAI_MODEL = 'gpt-4'
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

PROMPT_COUNTRY_INFO =""" Provide information about {country}. {format_instructions}
If the country does not exists, make up a country using anime names"""

def main():
    llm = ChatOpenAI(openai_api_key = OPENAI_API_KEY, model_name = OPENAI_MODEL)
    parser = PydanticOutputParser(pydantic_object=Country)


    # get user input 
    country = input(" Enter the name of the country ")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_COUNTRY_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages = [message])
    chat_prompt_with_values = chat_prompt.format_prompt(country = country, format_instructions = parser.get_format_instructions())

    response = llm(chat_prompt_with_values.to_messages())
    data = parser.parse(response.content)
    print(f'The capital of {data.name} is {data.capital}')

if __name__ == "__main__": 
    main()  