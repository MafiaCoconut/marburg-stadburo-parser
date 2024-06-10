import os

from icecream import ic
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def get_selenium_driver():
    FF_OPTIONS = [
        # '--headless',
        '--no-sandbox',
        '--accept-cookies'
        '--disable-xss-auditor',
        '--disable-web-security',
        '--ignore-certificate-errors',
        '--log-level=1',
        '--disable-notifications'
    ]

    SET_PREF = {
        'general.useragent.override': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'permissions.default.desktop-notification': 1,
        'dom.webnotifications.enabled': 1,
        'dom.push.enabled': 1,
        'intl.accept_languages': 'en-US'
    }

    options = FirefoxOptions()
    print(os.getenv("DEVICE"))
    if os.getenv("DEVICE") == "Ubuntu":
        options.binary_location = "/usr/bin/firefox"

        # current_directory = os.path.dirname(os.path.realpath(__file__))
        # current_directory = current_directory[:current_directory.rfind('/')]
        # print(current_directory)
        # ic(f"current_directory: {current_directory}")
        # geckodriver_path = os.path.join(current_directory, "geckodriver")
        # print(geckodriver_path)
        # ic(f"geckodriver path: {geckodriver_path}")

        geckodriver_path = "/usr/local/bin/geckodriver"
    # elif os.getenv("DEVICE") == "RaspberryTest":
    elif os.getenv("DEVICE") == "Raspberry" or os.getenv("DEVICE") == "RaspberryTest":
        geckodriver_path = "/app/geckodriver"
    else:
        raise Exception("Неправильный ENV DEVICE")

    [options.add_argument(opt) for opt in FF_OPTIONS]
    [options.set_preference(key, value) for key, value in SET_PREF.items()]

    driver = webdriver.Firefox(service=Service(geckodriver_path), options=options)

    return driver

if __name__ == '__main__':
    driver = get_selenium_driver()
    driver.get('http://www.python.org')