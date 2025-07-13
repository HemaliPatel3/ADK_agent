from google.adk import Agent
from google.adk.tools import google_search

search_agent = Agent(
    model = 'gemini-2.0-flash',
    name = 'search_agent',
    instruction= 'you extract insights from PDFs.',
    tools=[google_search]
)