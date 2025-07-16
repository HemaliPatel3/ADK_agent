from google.adk import Agent
from google.adk.tools import google_search
from google.adk.agents import SequentialAgent

search_agent = Agent( 
    model = "gemini-2.0-flash", 
    name = "search_agent" , 
    instruction = "You are a helpful assistant that explains code in simple language.hen given code, break it down step by step, describe what it does,give tips on how to improve or rewrite it.", 
    output_key="code_agent"
    )


learn_agent = Agent( 
    model = "gemini-2.0-flash", 
    name = "learn_agent" , 
    instruction = """ based on the code {code_agent} to find learning resources , You are an assistant that helps users learn programming, suggest short explanations and recommend YouTube videos, Google search queries,or beginner tutorials for that topic. """, 
    tools = [google_search]
    )

Sequentia_processing_stage = SequentialAgent( 
    name="Sequentia_processing", 
    sub_agents=[search_agent, learn_agent], 
    description="Process files and text separately, save outputs.",
    )

root_agent = Sequentia_processing_stage