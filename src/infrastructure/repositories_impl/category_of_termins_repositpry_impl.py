from sqlalchemy import select

from application.repositories.category_of_termins_repository import CategoryOfTerminsRepository
from infrastructure.db.base import session_factory
from infrastructure.db.models.categories_of_termins_orm import CategoriesOfTerminsOrm


class CategoryOfTerminsRepositoryImpl(CategoryOfTerminsRepository):
    @staticmethod
    def get_name(category_id: int):
        with session_factory() as session:
            query = (select(CategoriesOfTerminsOrm.name).filter(CategoriesOfTerminsOrm.category_id == category_id))
            result = session.execute(query)
            return result.scalars().all()[0]


