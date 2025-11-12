def test_read_hands_endpoint(client, game_factory, hand_factory):
    game = game_factory()
    for _ in range(4):
        hand_factory(game_id=game.id)

    response = client.get("/hands")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 4
    assert all("id" in hand for hand in data)
    assert all("player_slot" in hand for hand in data)
    assert all("score" in hand for hand in data)
    assert data[0]["score"] == 123
    assert all("created_at" in hand for hand in data)


def test_read_hands_empty(client, game_factory):
    game_factory()

    response = client.get("/hands")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 0
    assert data == []
