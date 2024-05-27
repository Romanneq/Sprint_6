import allure
from pages.main_page import MainPageSamokat
from selenium import webdriver
from pages.order_page_who_is_the_scooter_for import OrderPageWhoIsTheScooterFor



class TestButtons:

    driver = None
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Тестирование кнопки "Заказать" в шапке страницы')
    def test_display_form_who_is_the_scooter_click_on_button_order_in_header_page(self):
        main_page_obj = MainPageSamokat(self.driver)
        main_page_obj.click_button_order_in_header_page()
        order_page_obj = OrderPageWhoIsTheScooterFor(self.driver)
        assert order_page_obj.display_element_order_page()

    @allure.title('Тестирование кнопки "Заказать" в рабочей области страницы')
    def test_display_form_who_is_the_scooter_click_on_button_order_in_work_area_page(self):
        main_page_obj = MainPageSamokat(self.driver)
        main_page_obj.click_button_order_in_work_page()
        order_page_obj = OrderPageWhoIsTheScooterFor(self.driver)
        assert order_page_obj.display_element_order_page()

    @classmethod
    def teardown_class(cls):
        # закрыли браузер Firefox
        cls.driver.quit()