import pytest


@pytest.mark.usefixtures("termins_service, set_category_of_termins")
class TestGetTerminsList:
    @staticmethod
    @pytest.mark.parametrize(
        "termins_list",
        [
            "adressanderung",
            "eat_abholung",
            "registration_office",
            "others"
        ]
    )
    def get_termins_list_with_data(termins_service, termins_list):
        category_of_termins, test_termins = termins_list
        termins_service.save_termins(test_termins)

        termins = termins_service.get_termins_obj_list(category_of_termins=category_of_termins)
        for i, termin in termins:
            print(termin)
            print(test_termins[i])
            assert test_termins[i] == termin



        """
        ставим данные +
        получаем данные
        сверяем полученные данные с изначальными
        """

    @staticmethod
    @pytest.mark.parametrize
    def get_termins_list_without_data():
        pass


