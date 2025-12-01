Multi-Agent Meal Recommendation System with Recipe Search

A Google-ADK + Gemini powered AI system for personalized weekly meal plans
Overview

This project is a fully automated AI-driven meal planning system built using:

Google ADK (Agent Development Kit)

Gemini 2.5 Flash

Multi-agent orchestration

Automatic recipe discovery

Natural-language user input

The system reads a user’s dietary preferences, searches for suitable recipes, and generates a structured 7-day breakfast/lunch/dinner plan using a collaborative chain of LLM-powered agents.


Why Multi-Agent?

Instead of a single large prompt, the workflow is broken into autonomous agents:

Agent	Responsibility
Root Agent	Orchestrates full workflow & returns final output
Planner Agent	Reads input → calls recipe agent → builds weekly plan
Recipe Search Agent	Finds, filters, and structures recipe options

This modular structure increases accuracy, maintainability, scalability, and error-resilience.


System Architecture

USER INPUT
    │
    ▼
ROOT AGENT
    │
    ▼
PLANNER AGENT ─── calls ───► RECIPE SEARCH AGENT
    │                               │
    │◄────────────── returns recipes │
    ▼
GENERATED 7-DAY MEAL PLAN
    │
    ▼
FINAL JSON OUTPUT




Tech Stack
Python 3.13

Google ADK

Gemini 2.5 Flash


JSON-based inter-agent communication

Installation
git clone https://github.com/yourusername/meal-planner.git
cd meal-planner

python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# OR
.venv\Scripts\activate      # Windows

pip install -r requirements.txt


Ensure that your environment contains google-generativeai and google-adk.

🔑Environment Setup

Create a .env file:

GOOGLE_API_KEY=your_api_key_here

▶️ How to Run
1. Start your FastAPI server (if included)
uvicorn main:app --reload

2. Or run the pipeline directly
from agents import root_agent

response = root_agent.run({
    "user_input": "I am vegetarian, allergic to peanuts. Make a weekly meal plan."
})

print(response)

📝 Sample Input
I am vegetarian, allergic to peanuts, prefer high protein meals, 
and love Indian and Mediterranean cuisine. Create a weekly meal plan.

📤 Sample Output (shortened)
{
  "meal_plan": {
    "monday": {
      "breakfast": "Greek Yogurt Parfait",
      "lunch": "Paneer Tikka Bowl",
      "dinner": "Mediterranean Chickpea Stew"
    }
  }
}

Project Structure
meal-planner/
│
├── agents/
│   ├── root_agent.py
│   ├── planner_agent.py
│   ├── recipe_agent.py
│   └── __init__.py
│
├── tools/
│   ├── google_search_helper.py
│
├── main.py
├── README.md
└── requirements.txt

 Error Handling

To prevent ADK tool failures:

Recipe agent always returns:

{ "recipes": [] }


if search fails.

Planner agent checks list length before iterating.

Root agent enforces final JSON output only.

No agent is allowed to ask the user questions mid-flow.

This removes common issues such as:

TypeError: 'NoneType' object is not iterable

🔮 Future Improvements

🥦 Nutrition & macros analysis

🛒 Automatic shopping list generation

🧮 Cost-based meal planning

📚 Storing recipes in a local vector database

🌍 Support for multilingual meal plans



📄 License

MIT License.
