from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.base import async_engine
from infrastructure.repositories_impl.category_of_termins_repositpry_impl import CategoryOfTerminsRepositoryImpl
from infrastructure.repositories_impl.termins_repository_impl import TerminsRepositoryImpl


def get_termins_repository() -> TerminsRepositoryImpl:
    session = AsyncSession(bind=async_engine, expire_on_commit=False)
    return TerminsRepositoryImpl(session=session)


def get_category_of_termins_repository() -> CategoryOfTerminsRepositoryImpl:
    session = AsyncSession(bind=async_engine, expire_on_commit=False)
    return CategoryOfTerminsRepositoryImpl(session=session)
