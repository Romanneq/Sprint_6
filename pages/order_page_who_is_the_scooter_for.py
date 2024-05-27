from locators.locators_order_scooter_form_who_is_the_scooter import LocatorsOrderPageWhoIsTheScooter
from helpers import fake_filling_form_who_is_the_scooter
from pages.BasePage import BasePage
from locators.locators_main_page import LocatorsMainPage
import allure



class OrderPageWhoIsTheScooterFor(BasePage): # Создали класс формы заказа самоката: "Для кого самокат?"

    def __init__(self, driver):
        self.driver = driver
    @allure.step('Метод wait формы "Для кого самокат"')
    def wait_element_on_order_page(self):
        return super().wait_element_page(LocatorsOrderPageWhoIsTheScooter.text_form_who_is_the_scooter_for)

    @allure.step('Метод отображения формы "Для кого самокат"')
    def display_element_order_page(self):
        return super().display_element_page(LocatorsOrderPageWhoIsTheScooter.text_form_who_is_the_scooter_for)

    @allure.step('Метод заполнения формы "Для кого самокат"')
    def completion_form_who_is_the_scooter_for(self):
        super().url_page()
        super().click_element_page(LocatorsMainPage.button_order_in_header)
        name, second_name, address, telephone = fake_filling_form_who_is_the_scooter()
        super().send_keys_element(LocatorsOrderPageWhoIsTheScooter.first_name_form_who_is_the_scooter, name)
        super().send_keys_element(LocatorsOrderPageWhoIsTheScooter.second_name_form_who_is_the_scooter, second_name)
        super().send_keys_element(LocatorsOrderPageWhoIsTheScooter.address_form_who_is_the_scooter, address)
        super().click_element_page(LocatorsOrderPageWhoIsTheScooter.field_metro_station_form_who_is_the_scooter)
        super().click_element_page(LocatorsOrderPageWhoIsTheScooter.station_metro_form_who_is_the_scooter)
        super().send_keys_element(LocatorsOrderPageWhoIsTheScooter.telephone_form_who_is_the_scooter_for, telephone)