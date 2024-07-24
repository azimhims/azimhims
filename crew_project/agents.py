from tools import txttool
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

import os

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5, verboe=True,temperature=0.5,google_api_key=os.getenv("GOOGLE_API_KEY"))

os.environ["GOOGLE_API_KEY"] = "AIzaSyDdAgfPfeCbNDl-rJ893Cxwnv7_i7z5skM"
# os.environ["OPENAI_MODEL_NAME"]="sk-proj-PKZWJ3gac9BSlz0kKZ8JT3BlbkFJTstwZrv5KFY8sRckJg1q"
read_agent = Agent(role="Reader",
                   goal="Read the article and provide a summary",
                   backstory="Expert in reading and summarizing articles",
                   verbose=True,
                   tools=[txttool],
                   llm=llm,
                   allow_delegation=True
                   )

write_agent= Agent(role="Writer",
                   goal="Write a blog post based on the article summary",
                   backstory="Expert in writing and editing content",
                   verbose=True,
                   tools=[txttool],
                   llm=llm,
                   allow_delegation=True
                   )