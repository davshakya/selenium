import pytest
# @pytest.fixture(scope="class")
# def setup():
#     print("This will run the fixture first...")
#     yield
#     print("This will run in end...")
    
@pytest.fixture(scope="module")
def setup():
    print("This will run the fixture first...")
    yield
    print("This will run in end...")
    
def pytest_html_report_title(report):
    report.title="My very own report" 
