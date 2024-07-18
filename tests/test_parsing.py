import pytest


@pytest.mark.usefixtures("termins_service", "set_category_of_termins")
class TestParseStadburo:
    @staticmethod
    @pytest.mark.parametrize(
        "category_id",
        [
            1,
            2,
            3,
            4,
        ]
    )
    def test_parse_adressanderung(termins_service, category_id):
        termins_service.parse_termins_category(termin_category_id=category_id)

        termins = termins_service.get_termins_obj_list(category_of_termins=category_id)
        assert len(termins) > 0



