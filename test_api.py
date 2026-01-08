from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_aaa():
    response = client.get("/aaa")
    assert response.status_code == 200
    assert response.json() == {"message": "this is aaa"}


