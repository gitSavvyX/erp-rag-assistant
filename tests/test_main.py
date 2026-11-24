from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Healthy"

def test_ask_endpoint_missing_api_key():
    # This tests if the API handles missing keys securely
    response = client.post("/ask", json={"question": "What are the sales?"})
    assert response.status_code in [500, 422]
