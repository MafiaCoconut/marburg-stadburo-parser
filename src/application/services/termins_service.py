from application.interfaces.parser_interface import TerminsParserInterface
from application.repositories.termins_repository import TerminsRepository
from application.use_cases.get_termins_use_case import GetTerminsUseCase
from application.use_cases.parse_termins_use_case import ParseTerminsUseCase
from application.use_cases.save_termins_use_case import SaveTerminsUseCase


class TerminsService:
    def __init__(self,
                 termins_repository: TerminsRepository,
                 termins_parser_interface: TerminsParserInterface,
                 ):
        self.termins_repository = termins_repository
        self.termins_parser_interface = termins_parser_interface

        self.get_termins_use_case = GetTerminsUseCase(self.termins_repository)
        self.save_termins_use_case = SaveTerminsUseCase(self.termins_repository)
        self.parse_termins_use_case = ParseTerminsUseCase(self.termins_parser_interface)

    def parse_termin_category(self, termin_category_id: int):

        self.termins_parser_interface.parse()
