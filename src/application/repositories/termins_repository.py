from abc import ABC, abstractmethod
from domain.entities.termin import Termin


class TerminsRepository(ABC):
    @staticmethod
    @abstractmethod
    def get_all() -> list[Termin]:
        pass

    @staticmethod
    @abstractmethod
    def get_by_type(category_id: int) -> list[Termin]:
        pass

    @staticmethod
    @abstractmethod
    def save(termin: Termin) -> None:
        pass

    @staticmethod
    @abstractmethod
    def save_many(termins: list[Termin]) -> None:
        pass

    @staticmethod
    @abstractmethod
    def delete_all() -> None:
        pass

    @staticmethod
    @abstractmethod
    def delete_by_category(category_id: int) -> None:
        pass

    @staticmethod
    @abstractmethod
    def delete(termin_id: int) -> None:
        pass





