import pytest


@pytest.mark.usefixtures("termins_service", "set_category_of_termins")
class TestGetTerminsList:
    @staticmethod
    @pytest.mark.parametrize(
        "termins_list",
        [
            "adressanderung",
            "eat_abholung",
            "registration_office",
            "others"
        ],
        indirect=True
    )
    def test_get_termins_list_with_data(termins_service, termins_list):
        category_of_termins, test_termins = termins_list
        termins_service.save_termins(test_termins)

        termins = termins_service.get_termins_obj_list(category_of_termins=category_of_termins)
        print("termins: ", termins)
        print(type(termins))
        for i, termin in enumerate(termins):
            print("termin: ", termin)
            print("test_termins[i]: ", test_termins[i])
            assert test_termins[i] == termin

    @staticmethod
    def test_get_termins_list_without_data(termins_service, translation_service):
        termins = termins_service.get_category_of_termins_data(category_of_termins=1, locale='en')

        assert termins == translation_service.translate(message_id="lack-of-terms",locale='en')

    @staticmethod
    @pytest.mark.parametrize(
        "termins_list",
        [
            "adressanderung",
            "eat_abholung",
            "registration_office",
            "others"
        ],
        indirect=True
    )
    def test_get_category_of_termins_text(termins_service, translation_service, termins_list):
        category_of_termins, test_termins = termins_list
        termins_service.save_termins(test_termins)
        for language in ['ru', 'en', 'de', 'uk', 'ar']:
            termins = termins_service.get_category_of_termins_data(
                category_of_termins=category_of_termins, locale=language
            )

            assert isinstance(termins, str)





