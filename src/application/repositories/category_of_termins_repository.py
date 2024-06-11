from abc import ABC, abstractmethod


class CategoryOfTerminsRepository(ABC):
    @staticmethod
    @abstractmethod
    def get_name(category_id: int):
        pass
