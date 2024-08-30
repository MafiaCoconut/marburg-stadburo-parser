from abc import ABC, abstractmethod


class TerminsParserInterface(ABC):
    @abstractmethod
    async def parse(self) -> dict:
        pass
