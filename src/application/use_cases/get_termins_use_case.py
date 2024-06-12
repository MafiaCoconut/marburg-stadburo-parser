from application.repositories.category_of_termins_repository import CategoryOfTerminsRepository
from application.repositories.termins_repository import TerminsRepository
from application.services.translation_service import TranslationService


class GetTerminsUseCase:
    def __init__(self,
                 termins_repository: TerminsRepository,
                 translation_service: TranslationService,
                 category_of_termins_repository: CategoryOfTerminsRepository
                 ):
        self.termins_repository = termins_repository
        self.category_of_termins_repository = category_of_termins_repository
        self.translation_service = translation_service

    def get_all(self):
        termins = self.termins_repository.get_all()
        return termins

    def get_type(self, category_of_termins: int, locale: str):
        termins = self.termins_repository.get_by_type(category_of_termins)
        if termins is not None:

            text = self.translation_service.translate(
                message_id="list-of-all-termins",
                locale=locale,
                termins_name=self.category_of_termins_repository.get_name(category_id=category_of_termins),
                time=termins[0].created_at.strftime("%H:%M"),
                day_last_activate=termins[0].created_at.strftime("%d.%m.%Y")
            ) + "\n\n"

            k = 0
            for i, termin in enumerate(termins):
                k += 1
                if termin.time.day != termins[i-1].time.day:
                    if text[-1] != '\n':
                        text += '\n'
                    text += f"\n<b>{termin.time.strftime('%d.%m.%Y')}<b>\n"
                    k = 1

                text += f"{termin.time.strftime('%H:%M')} "
                if k % 6 == 0:
                    text += '\n'


            """
            day
            termin1 termin2 termin3 termin4 termin5 termin6 
            """

        else:
            text = self.translation_service.translate(
                message_id="lack-of-terms",
                locale=locale)

        return text


