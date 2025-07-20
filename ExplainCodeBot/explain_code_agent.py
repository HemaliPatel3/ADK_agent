from google.adk import Agent
from.import prompt
from google.adk.tools import google_search
from google.adk.agents import SequentialAgent

expain_code_agent = Agent(
    model = "gemini-2.0-flash",
    name = "search_agent" ,
    instruction= prompt.EXPLAIN_CODE_PROMPT,
    output_key="code_analysis"
    )

learn_agent = Agent(
    model = "gemini-2.0-flash",
    name = "learn_agent" ,
    instruction=prompt.LEARN_AGENT_PROMPT,
    tools = [google_search],
    output_key="learning_resources"
)

time_table_agent = Agent(
    model = "gemini-2.0-flash",
    name = "learn_agent" ,
    instruction=prompt.TIME_TABLE_AGENT_PROMPT
)

Sequentia_processing_stage = SequentialAgent(
    name="Sequentia_processing",
    sub_agents=[expain_code_agent, learn_agent, time_table_agent],
    description="Process files and text separately, save outputs.",
)

root_agent = Sequentia_processing_stage
