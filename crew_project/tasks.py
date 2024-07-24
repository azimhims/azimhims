from crewai import Task
from agents import read_agent
from tools import txttool




read_task = Task(
    description = "Read this article and provide a summary of the article",
    agent = read_agent,
    expected_output = "A summary of the article",
    output_file="summary.txt",
    tools=[txttool]

)

write_task = Task(
    description = "Write a blog post based on the summary of the article",
    agent = read_agent,
    expected_output = "A blog post",
    output_file="blogpost.txt",
    tools=[txttool]
)