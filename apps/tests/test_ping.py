import pytest
import json


def test_ping_pong_status(test_app):
    response = test_app.get(
        "/ping",
        data=json.dumps({"message": "ping"})
    )
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
