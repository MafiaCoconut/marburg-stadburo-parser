from application.repositories.termins_repository import TerminsRepository


class GetTerminsUseCase:
    def __init__(self, termins_repository: TerminsRepository):
        self.termins_repository = termins_repository

    def get_all(self):
        termins = self.termins_repository.get_all()
        return termins

    def get_type(self, type_of_termin: str):
        termins = self.termins_repository.get_by_type(type_of_termin)
        return termins
