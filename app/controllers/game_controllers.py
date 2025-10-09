from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.db.crud import game as game_crud, hand as hand_crud
from app.schemas.game import GameCreateSchema, GameOutSchema, GameDetailSchema
from app.schemas.hand import HandCreateSchema, HandOutSchema

router = APIRouter(prefix="/games", tags=["games"])


@router.post("/", response_model=GameOutSchema, operation_id="createGame")
def create_game(game: GameCreateSchema, db: Session = Depends(get_db)):
    """Creates and returns a game."""
    return game_crud.create_game(db, game)


@router.get("/{game_id}", response_model=GameDetailSchema, operation_id="readGameById")
def read_game_by_id(game_id: int, db: Session = Depends(get_db)):
    """Retrieve a single game by its ID."""
    db_game = game_crud.get_game_by_id(db, game_id)
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game


@router.get("/", response_model=List[GameOutSchema], operation_id="readGames")
def read_games(db: Session = Depends(get_db)):
    """Retrieve all games."""
    return game_crud.list_games(db)


@router.post(
    "/{game_id}/hands", response_model=HandOutSchema, operation_id="createGameHand"
)
def create_game_hand(
    hand: HandCreateSchema, game_id: int, db: Session = Depends(get_db)
):
    """Creates a hand and adds it to a specific game"""
    return hand_crud.create_hand(db, hand, game_id)
