import requests
from datetime import datetime
import pytest

@pytest.fixture
def url():
    return "https://www.google.com"

@pytest.fixture
def response(url):
    return requests.get(url)

def test_status_code(response):
    statusCode = response.status_code
    assert statusCode == 200

def test_headers(response):
    headers = response.headers
    assert 'Content-Type' in headers

def test_response_body(response):
    responseBody = response.text
    assert len(responseBody) > 0

def test_response_time(response):
    dateString = response.headers['Date']
    responseTime = datetime.strptime(dateString, "%a, %d %b %Y %H:%M:%S %Z")
    requestTime = datetime.strptime(response.request.headers['Date'], "%a, %d %b %Y %H:%M:%S %Z")
    elapsedTime = (responseTime - requestTime).total_seconds() * 1000
    assert elapsedTime < 1000
