from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.category_of_termins_repository import CategoryOfTerminsRepository
from application.repositories.termins_repository import TerminsRepository
from application.services.translation_service import TranslationService
from domain.entities.termin import Termin
from infrastructure.config.logs_config import log_decorator


class GetTerminsUseCase:
    def __init__(self,
                 repositories_provider: RepositoriesProvider,
                 translation_service: TranslationService,
                 category_of_termins_repository: CategoryOfTerminsRepository
                 ):
        self.repositories_provider = repositories_provider
        self.category_of_termins_repository = category_of_termins_repository
        self.translation_service = translation_service

    @log_decorator()
    async def get_all(self):
        termins_repository = self.repositories_provider.get_termins_repository()
        termins = await termins_repository.get_all()
        return termins

    @log_decorator()
    async def execute(self, category_of_termins_id: int):
        """
        Функция берёт данные из базы данных о выбранной категории и возвращает их в виде словаря
        :param category_of_termins_id: ID категории в базе данных
        :return: {'termins': list[Termin], 'category_of_termins': CategoryOfTermins, 'error': None}
        """
        termins_repository = self.repositories_provider.get_termins_repository()
        termins = await termins_repository.get_by_type(category_of_termins_id)
        category_of_termins = await self.category_of_termins_repository.get(category_id=category_of_termins_id)

        return {'termins': termins,
                'error': None,
                'category_of_termins': {
                    'category_id': category_of_termins.category_id,
                    'name': category_of_termins.name,
                    'created_at': category_of_termins.created_at


                }
        }

    @log_decorator()
    async def get_termins_obj_list(self, category_of_termins: int):
        termins_repository = self.repositories_provider.get_termins_repository()
        termins = await termins_repository.get_by_type(category_id=category_of_termins)
        new_termins = []
        for termin in termins:
            new_termins.append(
                Termin(
                    category_id=termin.category_id,
                    time=termin.time
                )
            )
        return new_termins
