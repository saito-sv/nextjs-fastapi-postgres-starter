import socketio
from app.services.chat_service import handle_message
from app.services.user_service import get_user_by_id
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import engine
import logging
from fastapi import HTTPException

sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=['http://localhost:3000'],
)

logger = logging.getLogger(__name__)

@sio.event
async def connect(sid, environ):
    try:
        print('Client connected:', sid)
    except Exception as e:
        logger.error(f"Error during connect: {e}")
        await sio.disconnect(sid)

@sio.event
async def disconnect(sid):
    try:
        print('Client disconnected:', sid)
    except Exception as e:
        logger.error(f"Error during disconnect: {e}")

@sio.event
async def message(sid, data):
    try:
        user_id = data.get('user_id')
        user_message = data.get('message')

        async with AsyncSession(engine) as db:
            user = await get_user_by_id(db, user_id)
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")

            response = await handle_message(db, user.id, user_message)
            await sio.emit('response', {'message': response}, room=sid)
    except HTTPException as http_exc:
        logger.error(f"HTTP error during message: {http_exc.detail}")
        await sio.emit('response', {'error': http_exc.detail}, room=sid)
    except Exception as e:
        logger.error(f"Unhandled error during message: {e}")
        await sio.emit('response', {'error': 'Internal Server Error'}, room=sid)

app = socketio.ASGIApp(sio)
