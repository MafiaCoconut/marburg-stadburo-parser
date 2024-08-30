from application.providers.repositories_provider import RepositoriesProvider
from application.repositories.termins_repository import TerminsRepository


class SaveTerminsUseCase:
    def __init__(self, repositories_provider: RepositoriesProvider):
        self.repositories_provider = repositories_provider

    async def save_many(self, termins: list) -> None:
        termins_repository = self.repositories_provider.get_termins_repository()
        await termins_repository.save_many(termins=termins)



