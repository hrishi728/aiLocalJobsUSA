import json

from langchain_core.tools import tool


_DEMO_JOBS = [
    {
        "title": "Junior Python Developer",
        "company": "Northstar Software",
        "location": "Seattle",
        "type": "Full-time",
    },
    {
        "title": "Data Analyst",
        "company": "Lakeview Health",
        "location": "Seattle",
        "type": "Full-time",
    },
    {
        "title": "Part-time Library Assistant",
        "company": "Madison Public Library",
        "location": "Madison",
        "type": "Part-time",
    },
]


@tool
def find_local_jobs(location: str, keyword: str = "") -> str:
    """Search the demo job postings by city and optional title or company keyword."""
    location_query = location.strip().casefold()
    keyword_query = keyword.strip().casefold()

    matches = [
        job
        for job in _DEMO_JOBS
        if location_query in job["location"].casefold()
        and (
            not keyword_query
            or keyword_query in job["title"].casefold()
            or keyword_query in job["company"].casefold()
        )
    ]

    if not matches:
        return "No matching demo postings found. These results are not live listings."

    return "Demo postings (not live listings): " + json.dumps(matches)
