from abc import ABC, abstractmethod


class CategoryOfTerminsRepository(ABC):
    @staticmethod
    @abstractmethod
    async def get_name(category_id: int):
        pass
