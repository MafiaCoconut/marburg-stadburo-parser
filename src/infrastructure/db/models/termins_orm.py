from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
# from infrastructure.db.base import
from infrastructure.db.models.orm_template_columns import intpk, created_at

from infrastructure.db.base import Base


class TerminsOrm(Base):
    __tablename__ = "termins"

    termin_id: Mapped[intpk]
    type: Mapped[str]
    time: Mapped[datetime]
    created_at: Mapped[created_at]


