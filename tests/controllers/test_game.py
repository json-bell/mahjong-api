def test_create_game_endpoint(client):
    payload = {}

    response = client.post("/games", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] > 0
    assert data["created_at"] is not None
