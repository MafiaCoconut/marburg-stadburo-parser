from abc import ABC, abstractmethod

from domain.entities.category_of_termin import CategoryOfTermins


class CategoryOfTerminsRepository(ABC):
    @staticmethod
    @abstractmethod
    async def get(category_id: int) -> CategoryOfTermins:
        pass
