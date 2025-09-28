from sqlalchemy.orm import Session
from app.db.session import SessionLocal, init_db
from app.db import models


def seed():
    db: Session = SessionLocal()
    init_db()  # create tables if not exist

    # Example: add a game with one hand
    game = models.Game()
    db.add(game)
    db.commit()
    db.refresh(game)

    print("Seeded game")


if __name__ == "__main__":
    seed()
