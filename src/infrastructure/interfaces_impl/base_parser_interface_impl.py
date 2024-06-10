import time

from selenium.webdriver.common.by import By

from application.interfaces.parser_interface import TerminsParserInterface
from domain.entities.termin import Termin


class BaseParserInterfaceImpl(TerminsParserInterface):
    def __int__(self):
        self.waiting_time = None
        self.driver = None

    def parse(self) -> dict:
        raise NotImplementedError("This method should be overridden in a subclass")

    def ablehnen_cookies(self):
        # отменить куки
        time.sleep(self.waiting_time)
        item = self.driver.find_element(By.XPATH, '//*[@id="cookie_msg_btn_no"]')
        item.click()
        time.sleep(self.waiting_time)

    def go_to_termins_menu(self):

        items = self.driver.find_element(By.XPATH, '//*[@id="OKButton"]')
        items.click()
        time.sleep(self.waiting_time)

        items = self.driver.find_element(By.XPATH, '//*[@id="suggest_location_content"]/form/input[4]')
        items.click()
        time.sleep(self.waiting_time)

    @staticmethod
    def refactor_item_to_termin_obj(item: dict) -> Termin:
        """
        Переделывает данные в объект Termin

        :param item: {"category_id": int, "time": datetime}
        :type item: dict
        :return: Entity object Termin
        :rtype: Termin
        """
        termin = Termin(
            category_id=item.get('category_id'),
            time=item.get('time')
        )
        return termin
