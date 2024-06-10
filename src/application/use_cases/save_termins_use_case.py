from application.repositories.termins_repository import TerminsRepository


class SaveTerminsUseCase:
    def __init__(self, termins_repository: TerminsRepository):
        self.termins_repository = termins_repository

    def save_many(self, termins: list, termin_category_id: int) -> None:
        self.termins_repository.save_many(termins=termins, category_id=termin_category_id)



