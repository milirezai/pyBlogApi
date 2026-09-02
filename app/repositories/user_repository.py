from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User

    
def get_by_id(db: Session, user_id: int):
    statement = select(User).where(User.id == user_id)
    return db.scalar(statement)

def get_by_email(db: Session, email: str):
    statement = select(User).where(User.email == email)
    return db.scalar(statement)

def create_user(db: Session, username: str, email: str, password_hash: str):
    user = User(username= username, email= email, password_hash= password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user    