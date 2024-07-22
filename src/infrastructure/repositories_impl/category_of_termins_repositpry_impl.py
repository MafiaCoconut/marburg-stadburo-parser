from sqlalchemy import select, delete, text

from application.repositories.category_of_termins_repository import CategoryOfTerminsRepository
from domain.entities.category_of_termin import CategoryOfTermins
from infrastructure.db.base import session_factory, async_session_factory
from infrastructure.db.models.categories_of_termins_orm import CategoriesOfTerminsOrm


class CategoryOfTerminsRepositoryImpl(CategoryOfTerminsRepository):
    @staticmethod
    def get_name(category_id: int):
        with async_session_factory() as session:
            query = (select(CategoriesOfTerminsOrm.name).filter(CategoriesOfTerminsOrm.category_id == category_id))
            result = session.execute(query)
            return result.scalars().all()[0]

    @staticmethod
    def save(category_of_termins: CategoryOfTermins):
        with async_session_factory() as session:
            category_of_termins_orm = CategoriesOfTerminsOrm(
                category_id=category_of_termins.category_id,
                name=category_of_termins.name
            )
            session.add(category_of_termins_orm)
            session.commit()

    @staticmethod
    def delete_all():
        with async_session_factory() as session:

            session.execute(delete(CategoriesOfTerminsOrm))
            session.execute(text(f"ALTER SEQUENCE {CategoriesOfTerminsOrm.__tablename__}_category_id_seq RESTART WITH 1;"))

            session.commit()

