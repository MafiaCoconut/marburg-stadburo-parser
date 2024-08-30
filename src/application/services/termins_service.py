from application.providers.categories_of_termins_provider import CategoriesOfTerminsProvider
from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.category_of_termins_repository import CategoryOfTerminsRepository
from application.repositories.termins_repository import TerminsRepository
from application.services.translation_service import TranslationService
from application.use_cases.get_termins_use_case import GetTerminsUseCase
from application.use_cases.parse_termins_use_case import ParseTerminsUseCase
from application.use_cases.save_termins_use_case import SaveTerminsUseCase
from domain.entities.termin import Termin


class TerminsService:
    def __init__(self,
                 repositories_provider: RepositoriesProvider,
                 category_of_termins_repository: CategoryOfTerminsRepository,
                 categories_of_termins_provider: CategoriesOfTerminsProvider,
                 translation_service: TranslationService
                 ):
        self.category_of_termins_repository = category_of_termins_repository
        self.repositories_provider = repositories_provider
        self.translation_service = translation_service
        self.categories_of_termins_provider = categories_of_termins_provider

        self.get_termins_use_case = GetTerminsUseCase(
            repositories_provider=self.repositories_provider,
            translation_service=self.translation_service,
            category_of_termins_repository=self.category_of_termins_repository
        )
        self.save_termins_use_case = SaveTerminsUseCase(repositories_provider=self.repositories_provider)
        self.parse_termins_use_case = ParseTerminsUseCase(
            repositories_provider=self.repositories_provider,
            save_termins_use_case=self.save_termins_use_case,
            categories_of_termins_provider=self.categories_of_termins_provider
        )
        # self.parse_termins_use_case = ParseTerminsUseCase(self.termins_parser_interface)



    async def parse_termins_category(self, termin_category_id: int):
        """
        Функция запускает парсинг конкретной столовой
        :param termin_category_id: ID категории
        :return: {'termins': list[Termin], 'error': str}
        """

        return await self.parse_termins_use_case.parse_termins_category(termin_category_id=termin_category_id)

    async def parse_all(self):
        """
        Функция запускает парсинг всех столовых
        """
        await self.parse_termins_use_case.parse_all()

    async def get_category_of_termins_data(self, category_of_termins_id: int):
        """
        Функция возвращает словарь данных о выбранной столовой
        :param category_of_termins_id:
        :return: {'termins': list[Termin], 'category_of_termins': CategoryOfTermins, 'error': None}
        """
        return await self.get_termins_use_case.execute(category_of_termins_id=category_of_termins_id)

    async def save_termins(self, termins: list[Termin]):
        termins_repository = self.repositories_provider.get_termins_repository()
        await termins_repository.save_many(termins)

    async def get_termins_obj_list(self, category_of_termins: int):
        return await self.get_termins_use_case.get_termins_obj_list(category_of_termins=category_of_termins)

