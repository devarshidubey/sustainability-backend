import pytest
import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app, db
from app.models.product import Product

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


def test_valid_product_score(client):
    payload = {
        "product_name": "Reusable Bottle",
        "materials": ["aluminum", "plastic"],
        "weight_grams": 300,
        "transport": "air",
        "packaging": "recyclable",
        "gwp": 5.0,
        "cost": 10.0,
        "circularity": 80.0,
        "weights": {"gwp":0.2, "circularity":0.5, "cost":0.3}
    }
    response = client.post("/score", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert "sustainability_score" in data
    assert "rating" in data
    assert "suggestions" in data


def test_missing_field(client):
    payload = {
        "materials": ["aluminum", "plastic"],
        "weight_grams": 300,
        "transport": "air",
        "packaging": "recyclable",
        "gwp": 5.0,
        "cost": 10.0,
        "circularity": 80.0
    }  # missing product_name
    response = client.post("/score", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "product_name" in data["errors"]

def test_invalid_weights(client):
    payload = {
        "product_name": "Reusable Bottle",
        "materials": ["aluminum"],
        "weight_grams": 200,
        "transport": "air",
        "packaging": "recyclable",
        "gwp": 5.0,
        "cost": 10.0,
        "circularity": 70.0,
        "weights": {"gwp":1.5, "circularity":0.5, "cost":0.3}
    }
    response = client.post("/score", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "gwp" in data["errors"]["weights"]
