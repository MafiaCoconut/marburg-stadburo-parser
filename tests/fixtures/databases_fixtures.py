import pytest

from sqlalchemy.orm import sessionmaker

from infrastructure.db.base import sync_engine

@pytest.fixture(scope="session")
def db_session():
    Session = sessionmaker(bind=sync_engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture(scope="function")
def termins_repository(db_session, monkeypatch):
    def mock_session_factory():
        return db_session

    # Подменяем session_factory на нашу фикстуру
    monkeypatch.setattr('src.repositories.termins_repository.session_factory', mock_session_factory)
