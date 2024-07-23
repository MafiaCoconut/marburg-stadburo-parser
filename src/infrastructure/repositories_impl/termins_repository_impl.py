from application.repositories.termins_repository import TerminsRepository
from domain.entities.termin import Termin
from infrastructure.db.base import sync_engine, session_factory, Base, async_session_factory
from sqlalchemy import select, delete

from infrastructure.db.models.termins_orm import TerminsOrm


class TerminsRepositoryImpl(TerminsRepository):
    @staticmethod
    async def get_all() -> list[Termin]:
        async with async_session_factory() as session:
            query = select(TerminsOrm)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_type(category_id: int) -> list[Termin]:
        async with async_session_factory() as session:
            query = (
                select(TerminsOrm)
                .filter(TerminsOrm.category_id == int(category_id))
            )
            res = await session.execute(query)
            return res.scalars().all()


    @staticmethod
    async def save(termin: Termin) -> None:
        async with async_session_factory() as session:
            termin_orm = TerminsOrm(
                category_id=termin.category_id,
                time=termin.time
            )
            session.add(termin_orm)
            await session.commit()

    @staticmethod
    async def save_many(termins: list[Termin]) -> None:
        async with async_session_factory() as session:
            for termin in termins:
                termin_orm = TerminsOrm(
                    category_id=termin.category_id,
                    time=termin.time
                )
                session.add(termin_orm)
            await session.commit()

    @staticmethod
    async def delete_all() -> None:
        async with async_session_factory() as session:
            query = delete(TerminsOrm)
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def delete_by_category(category_id: int) -> None:
        async with async_session_factory() as session:
            query = (
                delete(TerminsOrm)
                .filter(TerminsOrm.category_id == int(category_id))
            )
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def delete(termin_id: int) -> None:
        async with async_session_factory() as session:
            query = (
                delete(TerminsOrm)
                .filter(TerminsOrm.termin_id == int(termin_id))
            )
            await session.execute(query)
            await session.commit()

