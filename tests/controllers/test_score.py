def test_read_scoring_rules(client):
    response = client.get("/score/rules")

    assert response.status_code == 200
    data = response.json()

    assert len(data) >= 9
    rule = data["all_pungs"]
    assert rule["description"] is not None
    assert rule["slug"] is not None
    assert rule["score_value"] == 3
