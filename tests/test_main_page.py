import allure
import pytest
from data import ListData
from locators.locators_main_page import MainPageLocators


@pytest.mark.usefixtures("driver")
class TestQuestions:
    @allure.title(
        'Выпадающий список вопросов-ответов в разделе "Вопросы о важном"')
    @allure.description('На главной странице перейти к разделу, нажать на вопрос,'
                        ' при разворачивании выполняется отображение соответствующего ответа')
    @pytest.mark.parametrize("index,text", ListData.QUESTIONS_LIST)
    def test_get_answer_on_question(self, driver, base_page, main_page, index, text):
        base_page.scroll_to(MainPageLocators.FAQ)
        main_page.click_on_question(index)
        answer = main_page.get_answer_text()
        main_page.wait_for_get_answer()
        assert answer == text, f'Ответ на вопрос {index} соответвтствует ожидаемому'
