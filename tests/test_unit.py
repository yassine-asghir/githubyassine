from fastapi.testclient import TestClient
import pytest
from main import app, get_double
from random import randint

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World!"

def test_double():
    randomNumber = randint(0, 5)
    response = client.get(f"/{randomNumber}")
    assert response.status_code == 200
    assert response.json() == randomNumber * 2

def test_getdouble():
    randomNumber = randint(0, 5)
    assert get_double(randomNumber) == randomNumber * 2

