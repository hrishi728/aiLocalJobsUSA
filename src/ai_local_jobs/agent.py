import os

from langchain.agents import create_agent

from ai_local_jobs.tools import find_local_jobs


def create_job_agent():
    """Create an agent that searches the project's demo job postings."""
    return create_agent(
        model=os.getenv("OPENROUTER_MODEL", "inclusionai/ling-3.2-flash:free"),
        tools=[find_local_jobs],
        system_prompt=(
            "You help users search local job postings using the available tool. "
            "Always use the tool for job searches. The tool contains mock demo "
            "data only; clearly say results are not live job listings. If the "
            "user does not provide a location, ask for one."
        ),
    )
