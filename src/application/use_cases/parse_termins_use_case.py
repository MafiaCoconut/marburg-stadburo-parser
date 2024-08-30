from icecream import ic

from application.interfaces.parser_interface import TerminsParserInterface
from application.providers.categories_of_termins_provider import CategoriesOfTerminsProvider
from application.providers.repositories_provider import RepositoriesProvider
from application.use_cases.save_termins_use_case import SaveTerminsUseCase
from domain.entities.termin import Termin
from infrastructure.config.logs_config import log_decorator


class ParseTerminsUseCase:
    def __init__(
                self,
            # termins_parser: TerminsParserInterface,
            save_termins_use_case: SaveTerminsUseCase,
            repositories_provider: RepositoriesProvider,
            categories_of_termins_provider: CategoriesOfTerminsProvider,
    ):
        # self.termins_parser = termins_parser
        self.repositories_provider = repositories_provider
        self.save_termins_use_case = save_termins_use_case
        self.categories_of_termins_provider = categories_of_termins_provider

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
    def aufenthaltstitel_parser_interface(self):
        return self.categories_of_termins_provider.get_aufenthaltstitel_parser_interface()

    @log_decorator()
    async def parse_termins_category(self, termin_category_id: int):
        """
        Функция запускает парсинг конкретной столовой
        :param termin_category_id: ID категории
        :return: {'termins': list[Termin], 'error': str}
        """
        termins_repository = self.repositories_provider.get_termins_repository()
        await termins_repository.delete_by_category(category_id=termin_category_id)
        parse_use_case = None
        match termin_category_id:
            case 1:
                result = await self.adressanderung_parser_interface.parse()
            case 2:
                result = await self.eat_abholung_parser_interface.parse()
            case 3:
                result = await self.registration_office_parser_interface.parse()
            case 4:
                result = await self.others_parser_interface.parse()
            case 5:
                result = await self.aufenthaltstitel_parser_interface.parse()

        if result.get('termins') is not None:
            await self.save_termins_use_case.save_many(termins=result['termins'])
        return result

    @log_decorator()
    async def parse_all(self):
        """
        Функция запускает парсинг всех столовых
        """
        await self.parse_termins_category(1)
        await self.parse_termins_category(2)
        await self.parse_termins_category(3)
        await self.parse_termins_category(4)
        await self.parse_termins_category(5)
