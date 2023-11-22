import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_base_page import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    def wait_for_new_tab(self, number):
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(number))

    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 10).until(ec.url_to_be(url))

    @allure.step('Клик по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.SCOOTER_LOGO).click()

    @allure.step('Открыть страницу {page}')
    def open_page(self, page):
        self.driver.get(page)

    def click_cookie_button(self):
        self.driver.find_element(*BasePageLocators.COOKIE_BUTTON).click()

    @allure.step('Пролистать')
    def scroll_to(self, locator):
        field = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", field)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
