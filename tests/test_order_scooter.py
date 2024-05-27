import allure
from selenium import webdriver
from pages.order_page_who_is_the_scooter_for import OrderPageWhoIsTheScooterFor
from pages.order_page_about_rent import OrderPageAboutRent



class TestOrderFormWhoIsTheScooter:

    driver = None
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Метод создания заказа в Яндекс.Самокат')
    def test_order_scooter(self):
        order_page_who_is_the_scooter_for = OrderPageWhoIsTheScooterFor(self.driver)
        order_page_about_rent = OrderPageAboutRent(self.driver)
        order_page_who_is_the_scooter_for.completion_form_who_is_the_scooter_for()
        order_page_about_rent.completion_form_about_rent()
        assert order_page_about_rent.display_order_status()

    @classmethod
    def teardown_class(cls):
        # закрыли браузер Firefox
        cls.driver.quit()