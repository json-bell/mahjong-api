from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime, timezone


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    # wip # score = Column(Integer)
    # wip # round_wind: Column(Enum(WindValueDB, name="wind_enum"), nullable=False)
    # wip # east_player: Column(Integer)

    hands = relationship("Hand", back_populates="game")
    # wip # players = relationship("Player", back_populates="players")


class Hand(Base):
    __tablename__ = "hands"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    tiles = Column(String)  # JSON that parses to 4 melds + a pair
    score = Column(Integer)
    # wip # player_id = Column(Integer, ForeignKey("players.id"))
    # wip # stuff for history - seat wind, round wind, list of what score increases have been applied

    game = relationship("Game", back_populates="hands")
    # wip # player = relationship("Player", back_populates="players")


""" wip
class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(31))
    game_id = Column(Integer, ForeignKey("games.id"))
    player_index = Column(Integer)

    game = relationship("Game", back_populates="hands")
    hands = relationship("Hand", back_populates="game")
"""
