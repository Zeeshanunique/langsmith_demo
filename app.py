from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(

    [
        ("system","You are a helpul assistant. Please respond to the user request only based on the given context"),
        ("user","Question:{question}\nContext:{context}"),
    ]
)
model = ChatOpenAI(model='gpt-3.5-turbo')
output_parser = StrOutputParser()
chain = prompt|model|output_parser

question = "Can you summerize the speech?"
context = '''
We have identified five areas where India has a core competence for an integrated action: (1) Agriculture and food processing - we have to put a target of 360 million tons of food and agricultural production. Other areas of agriculture and agro food processing would bring prosperity to rural people and speed up the economic growth. (2) Reliable and quality electric power for all parts of the country. (3) Education and Healthcare - we have seen, based on the experience, education and healthcare are inter related and assist population control leads to social security and also national security. (4) Information Technology - This is one of our core competence. We believe, this area can be used to promote education in remote areas and also to create national wealth. (5) Strategic sectors - This area, fortunately, witnessed the growth in nuclear technology, space technology and defence technology.

These five areas are closely inter-related and lead to national, food, economic and security. A strong partnership among the R&D, academy, industry, business and the community as a whole with the Government departments and agencies will be essential to accomplish the vision.

Agriculture and food processing
'''
print(chain.invoke({"question":question,"context":context}))