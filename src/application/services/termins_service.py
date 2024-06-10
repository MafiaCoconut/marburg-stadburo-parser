from application.providers.categories_of_termins_provider import CategoriesOfTerminsProvider
from application.repositories.termins_repository import TerminsRepository
from application.use_cases.get_termins_use_case import GetTerminsUseCase
from application.use_cases.parse_termins_use_case import ParseTerminsUseCase
from application.use_cases.save_termins_use_case import SaveTerminsUseCase


class TerminsService:
    def __init__(self,
                 termins_repository: TerminsRepository,
                 categories_of_termins_provider: CategoriesOfTerminsProvider,
                 ):
        self.termins_repository = termins_repository
        self.categories_of_termins_provider = categories_of_termins_provider

        self.get_termins_use_case = GetTerminsUseCase(self.termins_repository)
        self.save_termins_use_case = SaveTerminsUseCase(self.termins_repository)
        # self.parse_termins_use_case = ParseTerminsUseCase(self.termins_parser_interface)

    @property
    def adressanderung_parser_interface(self):
        return self.categories_of_termins_provider.get_adressanderung_parser_interface()

    @property
    def eat_abholung_parser_interface(self):
        return self.categories_of_termins_provider.get_eat_abholung_parser_interface()

    @property
    def registration_office_parser_interface(self):
        return self.categories_of_termins_provider.get_registration_office_parser_interface()

    @property
    def others_parser_interface(self):
        return self.categories_of_termins_provider.get_others_parser_interface()

    def parse_termins_category(self, termin_category_id: int):
        parse_use_case = None
        match termin_category_id:
            case 1:
                parse_use_case = ParseTerminsUseCase(self.adressanderung_parser_interface)
            case 2:
                parse_use_case = ParseTerminsUseCase(self.eat_abholung_parser_interface)
            case 3:
                parse_use_case = ParseTerminsUseCase(self.registration_office_parser_interface)
            case 4:
                parse_use_case = ParseTerminsUseCase(self.others_parser_interface)

        if parse_use_case is not None:
            result = parse_use_case.execute()
            # print(result)
            if result['termins']:
                self.save_termins_use_case.save_many(termins=result['termins'], termin_category_id=termin_category_id)

            return result


