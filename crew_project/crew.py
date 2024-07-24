from crewai import Crew, Process
from agents import read_agent, write_agent
from tasks import read_task, write_task



crew = Crew(
    agents=[read_agent, write_agent],
    tasks=[read_task,write_task],
    verbose=True,
    process=Process.sequential
)

result = crew.kickoff()
print(result)