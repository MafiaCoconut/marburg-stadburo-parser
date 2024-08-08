from sqlalchemy.ext.asyncio import AsyncSession

from application.repositories.termins_repository import TerminsRepository
from domain.entities.termin import Termin
from infrastructure.db.base import sync_engine, session_factory, Base, async_session_factory
from sqlalchemy import select, delete

from infrastructure.db.models.termins_orm import TerminsOrm


class TerminsRepositoryImpl(TerminsRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[Termin]:
        async with self.session.begin():
            query = select(TerminsOrm)
            res = await self.session.execute(query)
            return [Termin(
                termin_id=termin.termin_id,
                category_id=termin.category_id,
                time=termin.time
            )for termin in res.scalars().all()]

    async def get_by_type(self, category_id: int) -> list[Termin]:
        async with self.session.begin():
            query = (
                select(TerminsOrm)
                .where(TerminsOrm.category_id == int(category_id))
            )
            res = await self.session.execute(query)
            return [Termin(
                termin_id=termin.termin_id,
                category_id=termin.category_id,
                time=termin.time,
                created_at=termin.created_at
            ) for termin in res.scalars().all()]

    async def save(self, termin: Termin) -> None:
        async with self.session.begin():
            termin_orm = TerminsOrm(
                category_id=termin.category_id,
                time=termin.time
            )
            self.session.add(termin_orm)
            await self.session.commit()

    async def save_many(self, termins: list[Termin]) -> None:
        async with self.session.begin():
            for termin in termins:
                termin_orm = TerminsOrm(
                    category_id=termin.category_id,
                    time=termin.time
                )
                self.session.add(termin_orm)
            await self.session.commit()

    async def delete_all(self) -> None:
        async with self.session.begin():
            query = delete(TerminsOrm)
            await self.session.execute(query)
            await self.session.commit()

    async def delete_by_category(self, category_id: int) -> None:
        async with self.session.begin():
            query = (
                delete(TerminsOrm)
                .where(TerminsOrm.category_id == int(category_id))
            )
            await self.session.execute(query)
            await self.session.commit()

    async def delete(self, termin_id: int) -> None:
        async with self.session.begin():
            query = (
                delete(TerminsOrm)
                .where(TerminsOrm.termin_id == int(termin_id))
            )
            await self.session.execute(query)
            await self.session.commit()

