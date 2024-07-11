from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.user_service import get_user_by_id
from pydantic import BaseModel

class UserRead(BaseModel):
    id: int
    username: str

router = APIRouter()

@router.get("/users/me", response_model=UserRead)
async def get_my_user(db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, 1)  # Getting the first user for simplicity

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserRead(id=user.id, username=user.username)
