import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_main_page import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def get_questions(self):
        return self.driver.find_elements(*MainPageLocators.QUESTIONS)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, index):
        questions = self.get_questions()
        questions[index - 1].click()

    @allure.step('Получить текст ответа')
    def get_answer_text(self):
        return self.driver.find_element(*MainPageLocators.ANSWER).text

    def wait_for_get_answer(self):
        WebDriverWait(self.driver, 25).until(ec.visibility_of_element_located(MainPageLocators.ANSWER))



    @allure.step('Клик по кнопке "Заказать" на странице')
    def click_order_button(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE).click()

    @allure.step('Клик по кнопке "Заказать" в шапке')
    def click_order_button_in_header(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_IN_HEADER).click()

    @allure.step('Получить текст заголовка главной страницы')
    def get_main_header_text(self):
        return self.driver.find_element(*MainPageLocators.HEADER_TEXT).text