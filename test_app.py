from app import app

def test_health():

    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    assert response.get_json()["status"] == "healthy"


def test_revenue():

    client = app.test_client()

    response = client.get("/revenue")

    assert response.status_code == 200

    assert response.get_json()["total_revenue"] == 150000