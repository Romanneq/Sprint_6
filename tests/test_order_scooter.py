import data
import allure
from selenium import webdriver
from pages.order_page_who_is_the_scooter_for import OrderPageWhoIsTheScooterFor
from pages.order_page_about_rent import OrderPageAboutRent
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_order_scooter_form_who_is_the_scooter import LocatorsOrderPageWhoIsTheScooter
from locators.locators_order_scooter_form_about_rent import LocatorsOrderPageAboutRent



class TestOrderFormWhoIsTheScooter:

    driver = None
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()
    @allure.title ('Метод создания заказа в Яндекс.Самокат')
    def test_order_scooter(self):
        self.driver.get(f'{data.URL}order')
        order_page_who_is_the_scooter_for = OrderPageWhoIsTheScooterFor(self.driver) # заполнение формы "Для кого самокат?"
        order_page_who_is_the_scooter_for.completion_form_who_is_the_scooter()
        self.driver.find_element(*LocatorsOrderPageWhoIsTheScooter.button_go_to_rental_form).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPageAboutRent.text_form_about_rent))
        order_page_about_rent = OrderPageAboutRent(self.driver) # заполнение формы "Про аренду"
        order_page_about_rent.completion_form_about_rent()
        displayed_order_status = self.driver.find_element(*LocatorsOrderPageAboutRent.order_status_window)
        assert displayed_order_status.is_displayed()

    @classmethod
    def teardown_class(cls):
        # закрыли браузер Firefox
        cls.driver.quit()