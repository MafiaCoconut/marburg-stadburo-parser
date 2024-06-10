from abc import ABC, abstractmethod

from domain.entities.termin import Termin


class TerminsRepository(ABC):
    @abstractmethod
    @staticmethod
    def get_all() -> list[Termin]:
        pass

    @abstractmethod
    @staticmethod
    def get_by_type(type_of_termin: str) -> list[Termin]:
        pass

    @abstractmethod
    @staticmethod
    def save(termin: Termin) -> None:
        pass

    @abstractmethod
    @staticmethod
    def save_many(termins: list[Termin]) -> None:
        pass

    @abstractmethod
    @staticmethod
    def delete_all() -> None:
        pass

    @abstractmethod
    @staticmethod
    def delete_by_type(type_of_termin: str) -> None:
        pass

    @abstractmethod
    @staticmethod
    def delete(termin_id: int) -> None:
        pass





