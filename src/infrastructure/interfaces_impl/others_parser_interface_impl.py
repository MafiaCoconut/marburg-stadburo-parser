from datetime import datetime
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from infrastructure.config.logs_config import log_decorator
from infrastructure.config.selenium_config import get_selenium_driver
from infrastructure.interfaces_impl.base_parser_interface_impl import BaseParserInterfaceImpl


class OthersParserInterface(BaseParserInterfaceImpl):
    def __init__(self):
        super().__init__()
        self.waiting_time = 2
        self.category_id = 4
        self.driver = None
        # print('----------')
        self.url_start = "https://termine-reservieren.de/termine/marburg/select2?md=7"

    @log_decorator(print_args=False, print_kwargs=False)
    async def parse(self) -> dict:
        result = {}
        try:
            self.driver = await get_selenium_driver()
            self.driver.get(self.url_start)
            self.ablehnen_cookies()
            result = self.get_termins()

        except Exception as e:
            pass
            # print(e)

        finally:
            self.driver.close()

        return result

    def get_termins(self) -> dict:
        items = self.driver.find_element(By.XPATH, f'//*[@id="cnc-22"]')
        items.click()
        time.sleep(self.waiting_time)
        count_days = 5

        self.go_to_termins_menu()

        try:
            self.check_termins_exist()
            return {"error": "no-free-termins"}
        except NoSuchElementException as e:
            pass

        flag = False
        result = []
        for d in range(1, count_days + 1):
            day = self.driver.find_element(By.XPATH, f'//*[@id="ui-id-{d}"]')
            if 'filter' in day.get_attribute('title'):
                if d == 1:
                    day_id = day.get_attribute('id')
                    flag = True
                else:
                    break
            else:

                day.click()
                time.sleep(self.waiting_time)

                day_id = day.get_attribute("aria-controls")
                title = day.get_attribute("title")
                day = title[title.find(' ') + 1:]

            self.get_termins_per_day(day_id=day_id, day=day, termins=result)
            if flag:
                break

        return {'termins': result}

    def get_termins_per_day(self, day_id: int, day: str, termins: list):
        row = len(self.driver.find_elements(By.XPATH, f'//*[@id="{day_id}"]/table/tbody/*'))
        for i in range(1, row + 1):
            column = len(self.driver.find_elements(By.XPATH, f'//*[@id="{day_id}"]/table/tbody/tr[{i}]/*'))
            for j in range(1, column):
                text = f'//*[@id="{day_id}"]/table/tbody/tr[{i}]/td[{j}]/form/button'
                try:
                    termin = self.driver.find_element(By.XPATH, text)
                    termin_time = termin.get_attribute('title')
                    item = {
                        "category_id": self.category_id,
                        "time": datetime.strptime(f"{day} {termin_time}", "%d.%m.%Y %H:%M")
                    }
                    termins.append(self.refactor_item_to_termin_obj(item=item))
                    # save_termin(type_of_termins, day, termin_time, weekday)
                except Exception as e:
                    pass

    def check_termins_exist(self):
        self.driver.find_element(By.XPATH, '//*[@id="inhalt"]/div[2]/h2')

