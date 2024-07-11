import random
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.chat import Chat

async def handle_message(db: AsyncSession, user_id: int, user_message: str) -> str:
    possible_responses = [
        "Sure, I can help with that.",
        "I'm not sure I understand. Can you rephrase?",
        "Let me look into that for you.",
        "Echo: {user_message} bot responded",
        "Can you provide more details?",
        "I’m here to assist you.",
        "Interesting, tell me more.",
        "Let's explore that further.",
        "Can you clarify your question?",
        "I’m happy to help with anything else."
    ]

    bot_response = random.choice(possible_responses).format(user_message=user_message)

    chat = Chat(user_message=user_message, bot_response=bot_response, user_id=user_id)
    db.add(chat)
    await db.commit()
    await db.refresh(chat)

    return bot_response

async def get_user_chats(db: AsyncSession, user_id: int):
    result = await db.execute(select(Chat).filter(Chat.user_id == user_id))
    return result.scalars().all()
