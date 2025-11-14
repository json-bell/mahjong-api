from datetime import datetime
from app.schemas import PlayerOutSchema, GameDetailSchema, GameOutSchema, PlayerCreateSchema
from app.domain import PlayerSlot


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
    GameDetailSchema.model_validate(data)
    assert data["id"] > 0
    assert data["hands"] == []
    assert data["players"] == []


def test_get_game_by_id_has_details(client, hand_factory, game_factory, player_factory):
    game = game_factory()

    player_names = ["player_1", "player_2", "player_3", "player_4"]
    [
        player_factory(game_id=game.id, name=player_names[i], player_slot=PlayerSlot(i + 1))
        for i in range(4)
    ]

    hand_factory(game_id=game.id)

    response = client.get(f"/games/{game.id}")

    assert response.status_code == 200
    data = response.json()

    assert len(data["hands"]) == 1
    db_hand = data["hands"][0]
    assert db_hand["game_id"] == game.id

    assert len(data["players"]) == 4
    for player in data["players"]:
        PlayerOutSchema.model_validate(player)


def test_get_game_returns_404_for_nonexistent_id(client):
    response = client.get("/games/8080")

    assert response.status_code == 404


def test_get_game_returns_422_for_invalid_id(client):
    response = client.get("/games/banana")

    assert response.status_code == 422


def test_create_game_with_players(client):
    payload = {
        "players": [
            PlayerCreateSchema(
                name=f"player_{i}",
                player_slot=PlayerSlot(i),
                score=0,
            ).__dict__
            for i in range(1, 5)
        ]
    }

    response = client.post("/games/", json=payload)

    assert response.status_code == 200
    data = response.json()

    created_game = GameOutSchema.model_validate(data)
    game_id = created_game.id

    response_2 = client.get(f"/games/{game_id}")
    game = GameDetailSchema.model_validate(response_2.json())
    assert all(isinstance(p, PlayerOutSchema) for p in game.players)
    assert len(game.players) == 4
