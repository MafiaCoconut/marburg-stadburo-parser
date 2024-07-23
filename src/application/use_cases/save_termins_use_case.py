from application.repositories.termins_repository import TerminsRepository


class SaveTerminsUseCase:
    def __init__(self, termins_repository: TerminsRepository):
        self.termins_repository = termins_repository

    async def save_many(self, termins: list) -> None:
        await self.termins_repository.save_many(termins=termins)



