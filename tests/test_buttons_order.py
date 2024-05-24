import allure
from pages.main_page import MainPageSamokat
from selenium import webdriver
from locators.locators_order_scooter_form_who_is_the_scooter import LocatorsOrderPageWhoIsTheScooter
import data



class TestButtons:

    driver = None
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Тестирование кнопки "Заказать" в шапке страницы')
    def test_display_form_who_is_the_scooter_click_on_button_order_in_header_page(self): # тест кликом на кнопку "Заказать" в шапке страницы
        self.driver.get(data.URL)
        order_page = MainPageSamokat(self.driver)
        order_page.click_on_button_order_in_header_page()
        displayed_text_in_the_form = 'Для кого самокат'
        text_form = self.driver.find_element(*LocatorsOrderPageWhoIsTheScooter.text_form_who_is_the_scooter_for).text
        assert displayed_text_in_the_form == text_form

    @allure.title('Тестирование кнопки "Заказать" в рабочей области страницы')
    def test_display_form_who_is_the_scooter_click_on_button_order_in_work_area_page(self): # тест кликом на кнопку "Заказать" в рабочей области страницы
        self.driver.get(data.URL)
        order_page = MainPageSamokat(self.driver)
        order_page.click_on_button_order_in_work_area_page()
        displayed_text_in_the_form = 'Для кого самокат'
        text_form = self.driver.find_element(*LocatorsOrderPageWhoIsTheScooter.text_form_who_is_the_scooter_for).text
        assert displayed_text_in_the_form == text_form

    @classmethod
    def teardown_class(cls):
        # закрыли браузер Firefox
        cls.driver.quit()