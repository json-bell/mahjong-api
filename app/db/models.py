from sqlalchemy import Integer, ForeignKey, VARCHAR, DateTime, func
from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from .base import Base


class GameModel(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    # wip # round_wind: Mapped[str] = mapped_column(Enum(WindValueDB, name="wind_enum"), nullable=False)
    # wip # east_player: Mapped[int] = mapped_column(Integer)

    hands: Mapped[list["HandModel"]] = relationship("HandModel", back_populates="game")
    players: Mapped[list["PlayerModel"]] = relationship(
        "PlayerModel", back_populates="game"
    )


class HandModel(Base):
    __tablename__ = "hands"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    game_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("games.id"), nullable=False
    )
    """Possibly we store this in an ideal case, so that we don't have to repeatedly make calls to Game"""
    # wip # player_id: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=False)
    player_slot: Mapped[int] = mapped_column(nullable=False)
    hand: Mapped[dict] = mapped_column(
        JSONB, nullable=False
    )  # HandSchema JSON - 4 melds & a pair
    score: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    # wip # stuff for history - seat wind, round wind, list of what score increases have been applied

    game: Mapped[list["GameModel"]] = relationship("GameModel", back_populates="hands")
    # wip # player: Mapped[list["PlayerModel"]] = relationship("PlayerModel", back_populates="hands")


class PlayerModel(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(VARCHAR(31))
    game_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("games.id"), nullable=False
    )
    player_slot: Mapped[int] = mapped_column(nullable=False)
    score: Mapped[int] = mapped_column(default=0)

    game: Mapped[list["GameModel"]] = relationship(
        "GameModel", back_populates="players"
    )
    # wip # hands: Mapped[list["HandModel"]] = relationship("HandModel", back_populates="player")
