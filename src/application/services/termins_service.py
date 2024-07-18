from application.providers.categories_of_termins_provider import CategoriesOfTerminsProvider
from application.repositories.category_of_termins_repository import CategoryOfTerminsRepository
from application.repositories.termins_repository import TerminsRepository
from application.services.translation_service import TranslationService
from application.use_cases.get_termins_use_case import GetTerminsUseCase
from application.use_cases.parse_termins_use_case import ParseTerminsUseCase
from application.use_cases.save_termins_use_case import SaveTerminsUseCase
from domain.entities.termin import Termin


class TerminsService:
    def __init__(self,
                 termins_repository: TerminsRepository,
                 category_of_termins_repository: CategoryOfTerminsRepository,
                 categories_of_termins_provider: CategoriesOfTerminsProvider,
                 translation_service: TranslationService
                 ):
        self.category_of_termins_repository = category_of_termins_repository
        self.termins_repository = termins_repository
        self.translation_service = translation_service
        self.categories_of_termins_provider = categories_of_termins_provider

        self.get_termins_use_case = GetTerminsUseCase(
            termins_repository=self.termins_repository,
            translation_service=self.translation_service,
            category_of_termins_repository=self.category_of_termins_repository
        )
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
        self.termins_repository.delete_by_category(category_id=termin_category_id)
        parse_use_case = None
        # print(termin_category_id)
        match termin_category_id:
            case 1:
                parse_use_case = ParseTerminsUseCase(self.adressanderung_parser_interface)
            case 2:
                parse_use_case = ParseTerminsUseCase(self.eat_abholung_parser_interface)
            case 3:
                parse_use_case = ParseTerminsUseCase(self.registration_office_parser_interface)
            case 4:
                parse_use_case = ParseTerminsUseCase(self.others_parser_interface)
        # print(parse_use_case.termins_parser)
        if parse_use_case is not None:
            result = parse_use_case.execute()
            if result.get('termins') is not None:
                self.save_termins_use_case.save_many(termins=result['termins'], termin_category_id=termin_category_id)
            if result.get('error') is None:
                result['error'] = "Произошла ошибка"
            return result

    def parse_all(self):
        self.parse_termins_category(1)
        self.parse_termins_category(2)
        self.parse_termins_category(3)
        self.parse_termins_category(4)

    def get_text_category_of_termins(self, category_of_termins: int, locale: str):
        return self.get_termins_use_case.get_type(category_of_termins=category_of_termins, locale=locale)

    def save_termins(self, termins: list[Termin]):
        self.termins_repository.save_many(termins)

    def get_termins_obj_list(self, category_of_termins: int):
        return self.get_termins_use_case.get_termins_obj_list(category_of_termins=category_of_termins)

