from ai_local_jobs.tools import find_local_jobs


def test_finds_jobs_by_location_and_keyword():
    result = find_local_jobs.invoke(
        {"location": "Seattle", "keyword": "python"}
    )

    assert "Junior Python Developer" in result
    assert "Lakeview Health" not in result
    assert "not live listings" in result


def test_returns_clear_message_when_no_jobs_match():
    result = find_local_jobs.invoke(
        {"location": "Seattle", "keyword": "accountant"}
    )

    assert "No matching demo postings found" in result
