# AI Local Jobs

A small learning project for building a LangChain agent that can search local
job postings. The included postings are **mock/demo data**, not live vacancies.

## What it does

- Accepts a question in the terminal.
- Gives a LangChain agent a `find_local_jobs` tool.
- Searches a small in-memory list by location and optional job keyword.

## Setup

Requirements: Python 3.12 or later and [uv](https://docs.astral.sh/uv/).

```powershell
uv sync
Copy-Item .env.example .env
```

Add your API key to `.env`. Choose a model available to your OpenAI account in
`OPENAI_MODEL` if the example model is not available to you. Do not commit `.env`
or share your API key.

## Run

From this directory:

```powershell
uv run python -m ai_local_jobs.cli
```

Try asking: `Find software engineering jobs in Seattle`.

## Test your API connection in a notebook

After `uv sync`, open `notebooks/01_test_api.ipynb` and select the project's
`.venv` Python kernel if prompted. The API smoke-test cell makes one small model
request. It reads the key from `.env` and does not print it.

## Project layout

```text
notebooks/
  01_test_api.ipynb  Checks the API connection and demonstrates the demo tool.
src/ai_local_jobs/
  agent.py       Creates the agent and provides its system prompt.
  cli.py         Reads one question and prints the agent's answer.
  tools.py       Contains the demo job data and search tool.
tests/
  test_tools.py  Tests the search behavior without calling an AI model.
```

## Learning roadmap

1. Replace the demo postings with data you are allowed to use, such as a
   manually maintained sample file or an official jobs API.
2. Add conversation memory with a thread ID.
3. Return a structured job-search result with Pydantic.
4. Add middleware to log or limit tool calls.
5. Explore an MCP tool only after the basic agent is working.

The agent currently searches only the mock records in `tools.py`. It does not
visit job websites or provide live job listings.

## Tests

```powershell
uv run pytest
```
