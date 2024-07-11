from sqlalchemy import String, ForeignKey, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Chat(Base):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_message: Mapped[str] = mapped_column(Text, nullable=False)
    bot_response: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))

    user: Mapped["User"] = relationship("User", back_populates="chats")

    def __repr__(self) -> str:
        return f"Chat(id={self.id!r}, user_id={self.user_id!r}, user_message={self.user_message!r}, bot_response={self.bot_response!r})"
