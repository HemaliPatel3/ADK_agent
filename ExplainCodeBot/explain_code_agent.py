from google.adk import Agent
from google.adk.tools import google_search

explain_code_agent = Agent(
    model = 'gemini-2.0-flash',
    name = 'explain_code_agent',
    instruction= '',
    tools=[google_search]
)

root_agent = explain_code_agent