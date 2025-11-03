from datetime import datetime
from app.schemas import HandOutSchema


def test_create_game(client):
    payload = {}

    response = client.post("/games", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["id"] > 0
    assert "created_at" in data
    datetime.fromisoformat(data["created_at"])


def test_get_games_endpoint(client, game_factory):
    for _ in range(5):
        game_factory()

    response = client.get("/games")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 5
    assert all("id" in game for game in data)
    assert all("hands" not in game for game in data)
    assert all("players" not in game for game in data)


def test_get_game_by_id(client, game_factory):
    game = game_factory()
    response = client.get(f"/games/{game.id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] > 0
    assert data["hands"] == []
    # wip # assert data["players"] == []


def test_get_game_by_id_has_details(client, hand_factory, game_factory):
    game = game_factory()
    hand_factory(game.id)
    # wip # player_names = ["player_1", "player_2", "player_3"]
    # wip # players = [player_factory(name=name) for name in player_names]

    response = client.get(f"/games/{game.id}")

    assert response.status_code == 200
    data = response.json()

    assert len(data["hands"]) == 1
    db_hand = data["hands"][0]
    hand_schema = HandOutSchema.model_validate(db_hand)
    assert hand_schema.game_id == game.id


def test_get_game_returns_404_for_nonexistent_id(client):
    response = client.get("/games/8080")

    assert response.status_code == 404


def test_get_game_returns_422_for_invalid_id(client):
    response = client.get("/games/banana")

    assert response.status_code == 422
