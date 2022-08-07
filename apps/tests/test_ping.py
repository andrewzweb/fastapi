import pytest
import json
from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ping_pong_status():
    response = client.get(
        "/ping",
        data=json.dumps({"message": "ping"})
    )
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
