from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
from app.api.routes import chat, user
from app.socket import sio, app as socket_app
from app.db.session import init_db
from app.seed.seed import seed_user_if_needed

fastapi_app = FastAPI()

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapi_app.include_router(chat.router)
fastapi_app.include_router(user.router)

@fastapi_app.on_event("startup")
async def on_startup():
    await init_db()
    seed_user_if_needed()

@fastapi_app.get("/")
async def root():
    return {"message": "Welcome to the Hello Patient Chatbot API"}

app = socketio.ASGIApp(sio, other_asgi_app=fastapi_app)
