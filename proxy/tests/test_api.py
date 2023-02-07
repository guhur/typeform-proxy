import string
import typing as t
import random
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..main import app
from ..settings import settings

client = TestClient(app)


def test_liveness():
    response = client.get("/liveness")
    assert response.status_code == 200, response.status_code
    assert response.text == '"OK"', response.text


def test_get_a_missing_form_id():
    response = client.get("/forms/missing_form_id")
    assert response.status_code == 404, response.status_code

    response = client.get(
        f"/forms/{settings.test_form_id}",
        params={"included_response_ids": "missing_response_id"},
    )
    assert response.status_code == 404, response.status_code


def test_get_responses():
    response = client.get(
        f"/forms/{settings.test_form_id}",
    )
    assert response.status_code == 404, response.status_code
