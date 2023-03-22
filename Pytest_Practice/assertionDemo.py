import requests
import pytest

@pytest.fixture
def demo_fixtures():
    print("This is fixtures#########################")

def test_demo2():
    url="https://reqres.in/api/users?page=2"
    response= requests.get(url)
    res=response.json()
    l = []
    for i in range(len(res["data"])):
        email = res["data"][i]["email"]
        l.append(email)
    assert "lindsay.ferguson@reqres.in" in l, "TC is failed"
    print("Passed")