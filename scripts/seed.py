from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.db import models
from app.db.base import Base
from app.config import settings


engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)
db: Session = SessionLocal()


def init_db():
    # create tables if not exist
    Base.metadata.create_all(bind=engine)


def seed():
    init_db()

    if settings.env == "test":
        print("Test environment: database created, skipping seeding")
        return

    game = models.Game()
    db.add(game)
    db.commit()
    db.refresh(game)

    hand = models.Hand(game_id=game.id, melds=[], pair={})
    db.add(hand)
    db.commit()
    db.refresh(hand)

    print(f"Seeded {settings.env} DB: Game {game.id}, Hand {hand.id}")


if __name__ == "__main__":
    seed()
