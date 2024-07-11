from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.chat_service import get_user_chats
from app.services.user_service import get_user_by_id

router = APIRouter()

@router.get("/chats")
async def read_user_chats(user_id: int = Query(...), db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await get_user_chats(db, user.id)
