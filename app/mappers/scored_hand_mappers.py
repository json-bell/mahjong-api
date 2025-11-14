from app.domain import ScoredHand, ScoringEngine, PlayerSlot
from app.schemas import ScoredHandCreateSchema, ScoredHandOutSchema
from app.db.models import HandModel
from typing import List
from typing import Optional
from datetime import datetime
from .hand_mappers import HandMapper

engine = ScoringEngine()


class ScoredHandMapper:
    @staticmethod
    def to_dict(scored_hand: ScoredHand) -> dict:
        return {
            "hand": HandMapper.to_dict(hand=scored_hand.hand),
            "score": scored_hand.score,
            "created_at": str(scored_hand.created_at),
            "player_slot": scored_hand.player_slot.value,
        }

    @staticmethod
    def from_schema(schema: ScoredHandCreateSchema) -> ScoredHand:
        assert not isinstance(schema, ScoredHandOutSchema), (
            "Prefer from_out_schema for Scored Hands if returned from DB"
        )
        hand = HandMapper.from_schema(schema=schema.hand)
        player_slot = schema.player_slot
        score = engine.score_hand(hand)

        return ScoredHand(hand, player_slot, score, created_at=None)

    @staticmethod
    def to_schema(
        scored_hand: ScoredHand, game_id: int, id: int
    ) -> ScoredHandOutSchema:
        return ScoredHandOutSchema(
            created_at=scored_hand.created_at,
            hand=HandMapper.to_schema(scored_hand.hand),
            player_slot=scored_hand.player_slot,
            score=scored_hand.score,
            # Persistence:
            game_id=game_id,
            id=id,
        )

    @staticmethod
    def to_create_schema(
        scored_hand: ScoredHand, game_id: int
    ) -> ScoredHandCreateSchema:
        return ScoredHandCreateSchema(
            hand=HandMapper.to_schema(scored_hand.hand),
            player_slot=scored_hand.player_slot,
            game_id=game_id,
        )

    @staticmethod
    def to_model(scored_hand: ScoredHand, game_id: int) -> HandModel:
        return HandModel(
            hand=HandMapper.to_dict(scored_hand.hand),
            player_slot=scored_hand.player_slot,
            score=scored_hand.score,
            game_id=game_id,
            **(
                {"created_at": scored_hand.created_at} if scored_hand.created_at else {}
            ),
        )

    @staticmethod
    def from_model(model: HandModel) -> ScoredHand:
        hand = HandMapper.from_dict(model.hand)
        return ScoredHand(
            hand=hand,
            score=model.score,
            created_at=model.created_at,
            player_slot=PlayerSlot(model.player_slot),
        )

    @staticmethod
    def from_short(
        melds: List[str],
        pair: str,
        player_slot: PlayerSlot = PlayerSlot(1),
        created_at: Optional[datetime] = None,
    ) -> ScoredHand:
        hand = HandMapper.from_short(melds, pair)

        score = engine.score_hand(hand)

        return ScoredHand(hand, player_slot, score, created_at)

    # Convenience round trip mappers:
    @staticmethod
    def model_to_schema(model: HandModel) -> ScoredHandOutSchema:
        return ScoredHandMapper.to_schema(
            ScoredHandMapper.from_model(model), game_id=model.game_id, id=model.id
        )

    @staticmethod
    def schema_to_model(schema: ScoredHandCreateSchema, game_id: int) -> HandModel:
        return ScoredHandMapper.to_model(
            ScoredHandMapper.from_schema(schema), game_id=game_id
        )
