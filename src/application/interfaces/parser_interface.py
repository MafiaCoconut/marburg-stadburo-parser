from abc import ABC, abstractmethod


class TerminsParserInterface(ABC):
    @abstractmethod
    def parse(self) -> dict:
        pass
