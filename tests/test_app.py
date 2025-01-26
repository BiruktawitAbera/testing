import sys
import os
# Add the parent directory (testing) to the sys.path so that app.py can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from app import app  # Now it will be able to find app.py in the testing folder


# This fixture creates a test client for making requests
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Example test for the root route
def test_hello_world(client):
    response = client.get('/')  # Make a GET request to '/'
    assert response.data == b'Hello, World!'  # Check that the response is 'Hello, World!'

# Example test for another route (replace '/another_route' with your actual route)
def test_another_route(client):
    response = client.get('/another_route')  # Make a GET request to '/another_route'
    assert response.status_code == 200  # Check that the status code is 200
