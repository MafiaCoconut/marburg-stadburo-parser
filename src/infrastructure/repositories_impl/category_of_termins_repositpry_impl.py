from sqlalchemy import select, delete, text
from sqlalchemy.ext.asyncio import AsyncSession

from application.repositories.category_of_termins_repository import CategoryOfTerminsRepository
from domain.entities.category_of_termin import CategoryOfTermins
from infrastructure.db.base import session_factory, async_session_factory
from infrastructure.db.models.categories_of_termins_orm import CategoriesOfTerminsOrm


class CategoryOfTerminsRepositoryImpl(CategoryOfTerminsRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_name(self, category_id: int) -> CategoryOfTermins:
        async with self.session.begin():
            query = (
                select(CategoriesOfTerminsOrm.name)
                .where(CategoriesOfTerminsOrm.category_id == category_id)
            )
            result = await self.session.execute(query)
            category_of_termins = result.scalars().first()
            return CategoryOfTermins(
                category_id=category_of_termins.category_id,
                name=category_of_termins.name,
                created_at=category_of_termins.created_at
            )

    async def save(self, category_of_termins: CategoryOfTermins):
        async with self.session.begin():
            category_of_termins_orm = CategoriesOfTerminsOrm(
                category_id=category_of_termins.category_id,
                name=category_of_termins.name
            )
            self.session.add(category_of_termins_orm)
            await self.session.commit()

    async def delete_all(self):
        async with self.session.begin():
            await self.session.execute(delete(CategoriesOfTerminsOrm))
            await self.session.execute(text(f"ALTER SEQUENCE {CategoriesOfTerminsOrm.__tablename__}_category_id_seq RESTART WITH 1;"))

            await self.session.commit()

