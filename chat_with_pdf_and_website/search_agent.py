from google.adk import Agent
from .import prompt
from google.adk.tools import google_search

search_agent = Agent(
    model = 'gemini-2.0-flash',
    name = 'search_agent',
    instruction= prompt.SEARCH_AGENT_PROMPT,
    tools=[google_search]
)

root_agent = search_agent