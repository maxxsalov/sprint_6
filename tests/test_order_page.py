import allure
import pytest

from locators.locators_main_page import MainPageLocators

from data import DataUrls, Persons
from data import TextData, RentalData


@pytest.mark.usefixtures("driver")
class TestOrderButton:
    
    @allure.title('Оформление заказа по кнопке "Заказать" в шапке страницы')
    @allure.description('Корректное заполнение всех полей заказа,'
                        ' после подтверждения отображается {TextData.SUCCESSFUL_ORDER_TEXT}')
    def test_order_button_on_header(self, driver, base_page, main_page, order_page):
        base_page.open_page(DataUrls.SCOOTER_URL)
        main_page.click_order_button_in_header()
        order_page.filling_form(Persons.PERSON_1, Persons.PERSON_1.get('number'))
        order_page.wait_for_rent_form()
        order_page.input_rental_information(RentalData.DATE_TODAY, RentalData.DATA_1)
        order_page.wait_for_confirm()
        order_page.click_confirmation_order()
        order_title = order_page.get_new_order_title()
        order_page.wait_for_order_completed()
        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title, 'Удачный заказ по кнопке "Заказать" в шапке'

    @allure.title('Оформление заказа по кнопке "Заказать" на главной странице')
    @allure.description('Корректное заполнение всех полей заказа,'
                        ' после подтверждения отображается {TextData.SUCCESSFUL_ORDER_TEXT}')
    def test_order_button_main_page_current_date_user_flow_positive(self, driver, base_page, main_page, order_page):
        base_page.scroll_to(MainPageLocators.ORDER_BUTTON_MAIN_PAGE)
        main_page.click_order_button()
        order_page.filling_form(Persons.PERSON_2, Persons.PERSON_2.get('number'))
        order_page.wait_for_rent_form()
        order_page.input_rental_information(RentalData.DATE_TOMORROW, RentalData.DATA_2)
        order_page.wait_for_confirm()
        order_page.click_confirmation_order()
        order_title = order_page.get_new_order_title()
        order_page.wait_for_order_completed()
        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title, 'Удачный заказ по кнопке "Заказать" после скролла'
