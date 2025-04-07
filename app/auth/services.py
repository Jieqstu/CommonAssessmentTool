from typing import Optional
from sqlalchemy.orm import Session
from app.models import User
from .security import verify_password, get_password_hash


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def create_user(
    db: Session, username: str, email: str, password: str, role: str
) -> User:
    hashed_pw = get_password_hash(password)
    new_user = User(
        username=username, email=email, hashed_password=hashed_pw, role=role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
