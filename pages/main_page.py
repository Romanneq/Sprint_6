import allure
from locators.locators_main_page import LocatorsMainPage
from pages.BasePage import BasePage



class MainPageSamokat(BasePage): # Создали класс главной страницы cервиса

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод скролла до футера страницы и отображение текста ответа на "Вопросы о важном"')
    def click_and_found_text(self, obj_q, obj_a):
        super().url_page()
        super().base_scroll_page(LocatorsMainPage.questions_about_important)
        super().click_element_page(obj_q)
        return super().base_text_element(obj_a)

    @allure.step('Метод клика на кнопку "Заказать" в рабочей области страницы')
    def click_button_order_in_work_page(self):
        super().url_page()
        super().base_scroll_page(LocatorsMainPage.button_order_in_work_area)
        super().click_element_page(LocatorsMainPage.button_order_in_work_area)

    @allure.step('Метод клика на кнопку заказать в шапке страницы')
    def click_button_order_in_header_page(self):
        super().url_page()
        super().click_element_page(LocatorsMainPage.button_order_in_header)
    @allure.step('Метод клика на "Яндекс" логотипа "Яндекс.Самокат"')
    def click_logo_yandex_yandex(self):
        super().url_page()
        super().click_element_page(LocatorsMainPage.logo_yandex_yandex)
        super().swith_another_tab()
    @allure.step('Метод клика на "Самокат" логотипа "Яндекс.Самокат"')
    def click_logo_yandex_samokat(self):
        super().url_page()
        super().click_element_page(LocatorsMainPage.logo_yandex_samokat)
        super().wait_element_page(LocatorsMainPage.locator_main_page)
    @allure.step('Метод отображения элемента на главной странице сервиса"')
    def display_main_page(self):
        return super().display_element_page(LocatorsMainPage.locator_main_page)