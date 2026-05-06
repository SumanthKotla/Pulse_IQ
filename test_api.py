import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"


def test_get_sales_data():
    r = client.get("/analytics/sales?days=7")
    assert r.status_code == 200
    data = r.json()
    assert "data" in data
    assert len(data["data"]) == 7


def test_get_kpis():
    r = client.get("/analytics/kpis")
    assert r.status_code == 200
    assert "kpis" in r.json()
    assert "total_revenue" in r.json()["kpis"]


def test_workflow_status():
    r = client.get("/workflows/status")
    assert r.status_code == 200
    assert "workflows" in r.json()
    assert r.json()["total_workflows"] == 4


def test_chat_demo_mode():
    r = client.post("/chat", json={"message": "What are my top KPIs?"})
    assert r.status_code == 200
    assert "response" in r.json()


def test_generate_report():
    r = client.post("/report/generate", json={
        "title": "Test Report",
        "metrics": ["total_revenue", "total_orders"],
        "period": "last_30_days"
    })
    assert r.status_code == 200
    assert "recommendations" in r.json()
