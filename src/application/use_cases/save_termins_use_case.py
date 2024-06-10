from application.repositories.termins_repository import TerminsRepository


class SaveTerminsUseCase:
    def __init__(self, termins_repository: TerminsRepository):
        self.termins_repository = termins_repository

    def execute(self, termins: dict) -> None:
        # self.termins_repository.save_all(termins)
        pass


