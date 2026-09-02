from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from app.repositories.user_repository import get_by_id,get_by_email,create_user

password_hash = PasswordHash.recommended()

def get_user(db: Session, user_id: int):
    return get_by_id(db,user_id)

def register_user(db: Session, username: str, email: str, password: str):
    existing_user = get_by_email(db,email)
    if existing_user:
        return None
    hashed_password = password_hash.hash(password)
    return create_user(db,username,email,hashed_password)
