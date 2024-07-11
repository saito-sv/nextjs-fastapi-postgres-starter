from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, index=True, nullable=False)
    chats: Mapped["Chat"] = relationship("Chat", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"
