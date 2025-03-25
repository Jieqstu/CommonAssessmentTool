"""
Database models module defining SQLAlchemy ORM models for the Common Assessment Tool.
Defines User, Client, and ClientCase models.
"""

from app.database import Base
from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey, CheckConstraint, Enum
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
import enum


class UserRole(str, enum.Enum):
    admin = "admin"
    case_worker = "case_worker"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)

    cases: Mapped[list["ClientCase"]] = relationship("ClientCase", back_populates="user")


class Client(Base):
    """
    Client model representing client data in the database.
    Each property is a demographic or capability field.
    """

    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    age: Mapped[int] = mapped_column(CheckConstraint("age >= 18"))
    gender: Mapped[int] = mapped_column(CheckConstraint("gender IN (1, 2)"))
    work_experience: Mapped[int] = mapped_column(CheckConstraint("work_experience >= 0"))
    canada_workex: Mapped[int] = mapped_column(CheckConstraint("canada_workex >= 0"))
    dep_num: Mapped[int] = mapped_column(CheckConstraint("dep_num >= 0"))
    canada_born: Mapped[bool]
    citizen_status: Mapped[bool]
    level_of_schooling: Mapped[int] = mapped_column(
        CheckConstraint("level_of_schooling BETWEEN 1 AND 14")
    )
    fluent_english: Mapped[bool]
    reading_english_scale: Mapped[int] = mapped_column(
        CheckConstraint("reading_english_scale BETWEEN 0 AND 10")
    )
    speaking_english_scale: Mapped[int] = mapped_column(
        CheckConstraint("speaking_english_scale BETWEEN 0 AND 10")
    )
    writing_english_scale: Mapped[int] = mapped_column(
        CheckConstraint("writing_english_scale BETWEEN 0 AND 10")
    )
    numeracy_scale: Mapped[int] = mapped_column(CheckConstraint("numeracy_scale BETWEEN 0 AND 10"))
    computer_scale: Mapped[int] = mapped_column(CheckConstraint("computer_scale BETWEEN 0 AND 10"))
    transportation_bool: Mapped[bool]
    caregiver_bool: Mapped[bool]
    housing: Mapped[int] = mapped_column(CheckConstraint("housing BETWEEN 1 AND 10"))
    income_source: Mapped[int] = mapped_column(CheckConstraint("income_source BETWEEN 1 AND 11"))
    felony_bool: Mapped[bool]
    attending_school: Mapped[bool]
    currently_employed: Mapped[bool]
    substance_use: Mapped[bool]
    time_unemployed: Mapped[int] = mapped_column(CheckConstraint("time_unemployed >= 0"))
    need_mental_health_support_bool: Mapped[bool]

    cases: Mapped[list["ClientCase"]] = relationship("ClientCase", back_populates="client")


class ClientCase(Base):
    """
    Model connecting a client to a case worker (user) with service and outcome info.
    """
    __tablename__ = "client_cases"

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)

    employment_assistance: Mapped[bool]
    life_stabilization: Mapped[bool]
    retention_services: Mapped[bool]
    specialized_services: Mapped[bool]
    employment_related_financial_supports: Mapped[bool]
    employer_financial_supports: Mapped[bool]
    enhanced_referrals: Mapped[bool]
    success_rate: Mapped[int] = mapped_column(CheckConstraint("success_rate BETWEEN 0 AND 100"))

    client: Mapped["Client"] = relationship("Client", back_populates="cases")
    user: Mapped["User"] = relationship("User", back_populates="cases")
