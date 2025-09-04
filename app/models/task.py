from datetime import datetime, timezone
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, DateTime
from app.db.session import Base

if TYPE_CHECKING:
    from app.models.user import User  # Solo para tipado, no en runtime


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    class TaskState(str):
        PENDIENTE = "pendiente"
        COMPLETADO = "completado"

    state: Mapped[TaskState] = mapped_column(
        String,
        nullable=False,
        default=TaskState.PENDIENTE,
        server_default=TaskState.PENDIENTE,
    )

    # Relación con User (bidireccional)
    owner: Mapped["User"] = relationship(back_populates="tasks")
