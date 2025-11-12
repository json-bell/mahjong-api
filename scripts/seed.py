from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.db.base import Base
from app.config import settings
from app.db.crud import hand as hand_crud, game as game_crud
from app.schemas import GameCreateSchema
from app.mappers import ScoredHandMapper


engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)
db: Session = SessionLocal()


def init_db():
    # create tables if not exist
    Base.metadata.create_all(bind=engine)


hand_dict = {
    "melds": [
        "CCi2",
        "CCi4",
        "PBa3",
        "PBa6",
    ],
    "pair": {"suit": "circle", "value": "5"},
}


def seed() -> None:
    init_db()

    if settings.env == "test":
        print("Test environment: database created, skipping seeding")
        return

    game = game_crud.create_game(db, GameCreateSchema())

    hand = ScoredHandMapper.to_create_schema(
        ScoredHandMapper.from_short(melds=["CCi2", "CCi4", "PBa3", "PBa6"], pair="Ci5"),
        game_id=game.id,
    )
    seeded_hand = hand_crud.create_hand(db, hand)

    print(f"Seeded {settings.env} DB: Game {game.id}, Hand {seeded_hand.id}")


if __name__ == "__main__":
    seed()
