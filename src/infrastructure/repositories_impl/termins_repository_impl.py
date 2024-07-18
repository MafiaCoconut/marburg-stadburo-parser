from application.repositories.termins_repository import TerminsRepository
from domain.entities.termin import Termin
from infrastructure.db.base import sync_engine, session_factory, Base
from sqlalchemy import select, delete

from infrastructure.db.models.termins_orm import TerminsOrm


class TerminsRepositoryImpl(TerminsRepository):
    @staticmethod
    def get_all() -> list[Termin]:
        with session_factory() as session:
            query = select(TerminsOrm)
            result = session.execute(query)
            return result.scalars().all()

    @staticmethod
    def get_by_type(category_id: int) -> list[Termin]:
        with session_factory() as session:
            query = (
                select(TerminsOrm)
                .filter(TerminsOrm.category_id == int(category_id))
            )
            res = session.execute(query)
            return res.scalars().all()


    @staticmethod
    def save(termin: Termin) -> None:
        with session_factory() as session:
            termin_orm = TerminsOrm(
                category_id=termin.category_id,
                time=termin.time
            )
            session.add(termin_orm)
            session.commit()

    @staticmethod
    def save_many(termins: list[Termin]) -> None:
        with session_factory() as session:
            for termin in termins:
                termin_orm = TerminsOrm(
                    category_id=termin.category_id,
                    time=termin.time
                )
                session.add(termin_orm)
            session.commit()

    @staticmethod
    def delete_all() -> None:
        with session_factory() as session:
            query = delete(TerminsOrm)
            session.execute(query)
            session.commit()

    @staticmethod
    def delete_by_category(category_id: int) -> None:
        with session_factory() as session:
            query = (
                delete(TerminsOrm)
                .filter(TerminsOrm.category_id == int(category_id))
            )
            session.execute(query)
            session.commit()

    @staticmethod
    def delete(termin_id: int) -> None:
        with session_factory() as session:
            query = (
                delete(TerminsOrm)
                .filter(TerminsOrm.termin_id == int(termin_id))
            )
            session.execute(query)
            session.commit()