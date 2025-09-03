from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.db.session import Base

if TYPE_CHECKING:
    from app.models.task import Task  # Solo para tipado, no en runtime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    # Relación con Task (bidireccional)
    tasks: Mapped[List["Task"]] = relationship(back_populates="owner")
