from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy import text


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=text("NOW()"))
    hands = relationship("Hand", back_populates="game")


class Hand(Base):
    __tablename__ = "hands"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    tiles = Column(String)  # Could be JSON or some serialized format
    score = Column(Integer)

    game = relationship("Game", back_populates="hands")
