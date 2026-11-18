"""Security utilities - password hashing and token management."""
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt, JWTError
from passlib.context import CryptContext
import secrets

from app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except JWTError:
        return None


def generate_session_id() -> str:
    return secrets.token_urlsafe(32)


def create_session_token(user_id: int, role: str, event_id: Optional[int] = None) -> str:
    data = {
        "sub": str(user_id),
        "role": role,
        "type": "session",
    }
    if event_id:
        data["event_id"] = event_id
    return create_access_token(data)


def verify_session_token(token: str) -> Optional[dict]:
    payload = decode_access_token(token)
    if payload and payload.get("type") == "session":
        return payload
    return None
