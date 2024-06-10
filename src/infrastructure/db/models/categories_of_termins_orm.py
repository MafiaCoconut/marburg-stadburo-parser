from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.db.base import Base
from infrastructure.db.models.orm_template_columns import intpk, created_at


class CategoriesOfTermins(Base):
    __tablename__ = "categories_of_termins"

    category_id: Mapped[intpk]
    name: Mapped[str]
    created_at: Mapped[created_at]

