from datetime import datetime
from sqlalchemy import ForeignKey, String, func, Numeric, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class TeamRoster(Base):
    __tablename__ = "team_rosters"
    
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"), primary_key=True)
    joined_at: Mapped[datetime] = mapped_column(server_default=func.now())

class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nickname: Mapped[str] = mapped_column(String, unique=True, index=True)
    riot_id: Mapped[str] = mapped_column(String, unique=True, index=True)
    
    puuid: Mapped[str] = mapped_column(String, unique=True, index=True)
    
    game_role: Mapped[str] = mapped_column(String)
    discord_tag: Mapped[str] = mapped_column(String, nullable=True)

    teams: Mapped[list["Team"]] = relationship(
        secondary="team_rosters", back_populates="players"
    )

class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    captain_id: Mapped[int] = mapped_column(ForeignKey("players.id"))

    players: Mapped[list["Player"]] = relationship(
        secondary="team_rosters", back_populates="teams"
    )
    captain: Mapped["Player"] = relationship(foreign_keys=[captain_id])

class Tournament(Base):
    __tablename__ = "tournaments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    entry_fee: Mapped[float] = mapped_column(Numeric(10, 2))
    status: Mapped[str] = mapped_column(String, default="upcoming")

class Match(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournaments.id"))
    opponent_name: Mapped[str] = mapped_column(String)
    team_score: Mapped[int] = mapped_column(Integer, default=0)
    opponent_score: Mapped[int] = mapped_column(Integer, default=0)
    match_result: Mapped[str] = mapped_column(String, nullable=True)

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournaments.id"))
    amount_paid: Mapped[float] = mapped_column(Numeric(10, 2))
    payment_status: Mapped[str] = mapped_column(String, default="completed") # pending, completed