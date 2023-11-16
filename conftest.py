import pytest
import datetime

from selenium import webdriver

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    page = BasePage(driver)
    return page


@pytest.fixture
def main_page(driver):
    questions = MainPage(driver)
    return questions


@pytest.fixture
def order_page(driver):
    order = OrderPage(driver)
    return order


@pytest.fixture
def get_date_today():
    return datetime.date.today().strftime('%d.%m.%Y')


@pytest.fixture
def get_date_tomorrow():
    return (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d.%m.%Y')
