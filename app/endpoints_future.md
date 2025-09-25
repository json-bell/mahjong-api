## GAME:

```json
{
  "game": {
    "PATCH": {
      "description": "Modifies a specific game"
    }
  }
}
```

## GET ALL GAME HANDS

```json
{
  "game/{game_id}/hands": {
    "GET": {
      "description": "List all hands for a game"
    }
  }
}
```

## GAME HAND endpoints:

```json
{
  "game/{game_id}/hands/{hand_id}": {
    "GET": {
      "description": "Get a specific hand for the current game"
    },
    "PATCH": {
      "description": "Modifies a specific hand for the current game"
    },
    "DELETE": {
      "description": "Deletes a hand from a game"
    }
  }
}
```

## Hand specific stuff (rly not that necessary)

```json
"hand": {
    "{hand_id}": {
        "GET": {
            "description": "Get a specific hand"
        },
        "DELETE": {
            "description": "Deletes a specific hand"
        }
    }
}

```
