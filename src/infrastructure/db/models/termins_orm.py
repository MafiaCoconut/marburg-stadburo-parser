from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text, ForeignKey

# from infrastructure.db.base import
from infrastructure.db.models.orm_template_columns import intpk, created_at

from infrastructure.db.base import Base


class TerminsOrm(Base):
    __tablename__ = "termins"

    termin_id: Mapped[intpk]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories_of_termins.category_id", ondelete="CASCADE"))
    time: Mapped[datetime]
    created_at: Mapped[created_at]


