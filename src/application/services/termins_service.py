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

    @property
    def auhenthaltstiteel_parser_interface(self):
        return self.categories_of_termins_provider.get_auhenthaltstiteel_parser_interface()

    async def parse_termins_category(self, termin_category_id: int):
        """
        Функция запускает парсинг конкретной столовой
        :param termin_category_id: ID категории
        :return: {'termins': list[Termin], 'error': str}
        """
        await self.termins_repository.delete_by_category(category_id=termin_category_id)
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
            case 5:
                parse_use_case = ParseTerminsUseCase(self.auhenthaltstiteel_parser_interface)
        # print(parse_use_case.termins_parser)
        if parse_use_case is not None:
            result = parse_use_case.execute()
            if result.get('termins') is not None:
                await self.save_termins_use_case.save_many(termins=result['termins'])
            # if result.get('error') is not None:
            #     result['error'] = "Произошла ошибка"
            return result

    async def parse_all(self):
        """
        Функция запускает парсинг всех столовых
        """
        await self.parse_termins_category(1)
        await self.parse_termins_category(2)
        await self.parse_termins_category(3)
        await self.parse_termins_category(4)

    async def get_category_of_termins_data(self, category_of_termins_id: int):
        """
        Функция возвращает словарь данных о выбранной столовой
        :param category_of_termins_id:
        :return: {'termins': list[Termin], 'category_of_termins': CategoryOfTermins, 'error': None}
        """
        return await self.get_termins_use_case.execute(category_of_termins_id=category_of_termins_id)

    async def save_termins(self, termins: list[Termin]):
        await self.termins_repository.save_many(termins)

    async def get_termins_obj_list(self, category_of_termins: int):
        return await self.get_termins_use_case.get_termins_obj_list(category_of_termins=category_of_termins)

