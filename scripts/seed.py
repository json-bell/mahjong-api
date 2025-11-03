from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.db.base import Base
from app.config import settings
from app.db.crud import hand as hand_crud, game as game_crud
from app.schemas import HandCreateSchema, GameCreateSchema


engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)
db: Session = SessionLocal()


def init_db():
    # create tables if not exist
    Base.metadata.create_all(bind=engine)


hand_dict = {
    "melds": [
        {"type": "chow", "tile": {"suit": "circle", "value": "2"}},
        {"type": "chow", "tile": {"suit": "circle", "value": "4"}},
        {"type": "pong", "tile": {"suit": "bamboo", "value": "3"}},
        {"type": "pong", "tile": {"suit": "bamboo", "value": "6"}},
    ],
    "pair": {"suit": "circle", "value": "5"},
}


def seed() -> None:
    init_db()

    if settings.env == "test":
        print("Test environment: database created, skipping seeding")
        return

    game = game_crud.create_game(db, GameCreateSchema())

    hand = HandCreateSchema.model_validate(hand_dict)
    hand = hand_crud.create_hand(db, hand, game.id)

    print(f"Seeded {settings.env} DB: Game {game.id}, Hand {hand.id}")


if __name__ == "__main__":
    seed()
