from dotenv import load_dotenv
from IPython.display import Image, display
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langchain_mcp_adapters.client import MultiServerMCPClient

from dotenv import load_dotenv
from gradio import Image

from ai_local_jobs.agent import create_job_agent


def main() -> None:
    load_dotenv()
    question = input("What local jobs are you looking for? ").strip()
    if not question:
        raise SystemExit("Please enter a job-search question.")

    agent = create_job_agent()
    result =  agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
