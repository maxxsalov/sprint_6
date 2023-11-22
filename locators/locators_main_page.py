from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ = By.XPATH, '//*[@class="accordion"]'  # Раздел "Вопросы о важном"
    QUESTIONS = By.XPATH, "//*[contains(@class, 'accordion__item')]"  # Вопросы
    ANSWER = By.XPATH, "//*[contains(@class, 'accordion__panel') and not(@hidden)]"  # Отображаемый ответ
    ORDER_BUTTON_MAIN_PAGE = By.XPATH, "//*[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    # Кнопка "Заказать" на странице
    ORDER_BUTTON_IN_HEADER = By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    # Кнопка "Заказать" в шапке
    HEADER_TEXT = By.XPATH, "//*[contains(@class, 'Home_Header')]"  # Заголовок на главной