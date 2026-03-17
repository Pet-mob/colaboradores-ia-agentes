from crewai import Crew
from agents.planner_agent import planner_agent
from agents.developer_agent import developer_agent
from agents.qa_agent import qa_agent
from tasks.dev_tasks import task_plan, task_dev, task_qa

def run_ai_team():

    crew = Crew(
        agents=[
            planner_agent,
            developer_agent,
            qa_agent
        ],
        tasks=[
            task_plan,
            task_dev,
            task_qa
        ],
        verbose=True
    )

    result = crew.kickoff()
    return result