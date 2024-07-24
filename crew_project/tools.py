# from crewai_tools import TXTSearchTool
# import os
# OPENAI_API_BASE='http://localhost:11434'
# OPENAI_MODEL_NAME='llama2'  # Adjust based on available model
# OPENAI_API_KEY='sk-proj-PKZWJ3gac9BSlz0kKZ8JT3BlbkFJTstwZrv5KFY8sRckJg1q'


# #os.environ["OPENAI_API_KEY"] = ""
# text = '''Python is a high-level, 
# interpreted programming language known for its simplicity and readability. 
# Created by Guido van Rossum and first released in 1991, 
# Python emphasizes code readability with its notable use of significant whitespace. 
# This makes it an excellent choice for beginners and experienced developers alike.'''

# # Initialize the tool to search within any text file's content the agent learns about during its execution
# #txttool = TXTSearchTool(txt = text)
# txttool = TXTSearchTool(txt=text, api_key=os.environ["OPEN_API_KEY"])
import os
#os.environ["OPENAI_API_KEY"] = "sk-None-4lw97lsXIknPBCXUTG6QT3BlbkFJWn4g7oVoCnrKHlE8nBs4"
from langchain_google_genai import ChatGoogleGenerativeAI
os.environ["GOOGLE_API_KEY"] = "AIzaSyDdAgfPfeCbNDl-rJ893Cxwnv7_i7z5skM"
os.environ["SERPER_API_KEY"] = "9cf2e60cd451582479e0efa36ed033ab259059ba" # serper.dev API key


#langchain-google-genai
#googleapi= "AIzaSyDdAgfPfeCbNDl-rJ893Cxwnv7_i7z5skM"


from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
import openai

llm = ChatGoogleGenerativeAI(model="gemini-pro", verboe=True,temperature=0.5,google_api_key=os.getenv("GOOGLE_API_KEY"))
search_tool = SerperDevTool()

research_agent = Agent(
  role='Researcher',
  goal='Find and summarize the latest AI news',
  backstory="""You're a researcher at a large company.
  You're responsible for analyzing data and providing insights
  to the business.""",
  verbose=True,
  tools=[search_tool],
  llm=llm,
  allow_delegation=True
)



task = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool]
)

crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=2
)

result = crew.kickoff()
print(result)