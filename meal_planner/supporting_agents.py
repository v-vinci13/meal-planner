from google.adk.agents import Agent
from .instruction import  RECIPE_INSTRUCTION, PLANNER_INSTRUCTION
from google.adk.tools.agent_tool import AgentTool
from .tools import google_search_helper
LLM="gemini-2.5-flash-lite"


 

recipe_search_agent = Agent(
    name="recipe_search_agent",
    model= LLM,
    description="An agent that searches for recipes based on user dietary profile.",
    instruction= RECIPE_INSTRUCTION,
    tools= [google_search_helper],
    output_key='recipes_output'

)


planner_agent = Agent(
    name="planner_agent",
    model=LLM,
    description="An agent that creates a 7-day meal plan based on user profile and recipes.",
    instruction= PLANNER_INSTRUCTION,
    tools=[AgentTool(agent=recipe_search_agent)],
    output_key='meal_plan'
    
)
print("PlannerAgent created successfully")
