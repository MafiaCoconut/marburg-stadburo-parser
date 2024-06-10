from application.interfaces.parser_interface import TerminsParserInterface
from domain.entities.termin import Termin


class ParseTerminsUseCase:
    def __init__(self, termins_parser: TerminsParserInterface):
        self.termins_parser = termins_parser

    def execute(self) -> dict:
        """
        Вызывает активацию парсинга терминов

        :return: Dictionary of termins {"type1": [], "type2": []}
        :rtype: dict
        """
        return self.termins_parser.parse()

