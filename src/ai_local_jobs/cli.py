from dotenv import load_dotenv

from ai_local_jobs.agent import create_job_agent


def main() -> None:
    load_dotenv()
    question = input("What local jobs are you looking for? ").strip()
    if not question:
        raise SystemExit("Please enter a job-search question.")

    agent = create_job_agent()
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
