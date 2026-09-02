from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.user_service import get_user as get_user_by_id,register_user
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix='/users',tags=['Users'])

@router.post('/',response_model= UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = register_user(db,user.username,user.email,user.password)
    if new_user is None:
        raise HTTPException(status_code= 404,detail="Email already registered")
    return new_user

@router.get('/{user_id}',response_model= UserResponse)
def get_user(user_id: int ,db: Session = Depends(get_db)):
    user = get_user_by_id(db,user_id)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user