from application.repositories.termins_repository import TerminsRepository
from domain.entities.termin import Termin


class TerminsRepositoryImpl(TerminsRepository):
    @staticmethod
    def get_all() -> list[Termin]:
        pass

    @staticmethod
    def get_by_type(type_of_termin: str) -> list[Termin]:
        pass

    @staticmethod
    def save(termin: Termin) -> None:
        pass

    @staticmethod
    def save_many(termins: list[Termin]) -> None:
        pass

    @staticmethod
    def delete_all() -> None:
        pass

    @staticmethod
    def delete_by_type(type_of_termin: str) -> None:
        pass

    @staticmethod
    def delete(termin_id: int) -> None:
        pass
