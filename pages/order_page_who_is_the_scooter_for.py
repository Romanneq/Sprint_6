from locators.locators_order_scooter_form_who_is_the_scooter import LocatorsOrderPageWhoIsTheScooter
from helpers import fake_filling_form_who_is_the_scooter



class OrderPageWhoIsTheScooterFor: # Создали класс формы заказа самоката: "Для кого самокат?"
    def __init__(self, driver):
        self.driver = driver

    def completion_form_who_is_the_scooter(self): # Метод заполнения формы "Для кого самокат?"
        name, second_name, address, telephone = fake_filling_form_who_is_the_scooter()
        self.driver.find_element(*LocatorsOrderPageWhoIsTheScooter.first_name_form_who_is_the_scooter).send_keys(name)
        self.driver.find_element(*LocatorsOrderPageWhoIsTheScooter.second_name_form_who_is_the_scooter).send_keys(second_name)
        self.driver.find_element(*LocatorsOrderPageWhoIsTheScooter.address_form_who_is_the_scooter).send_keys(address)
        self.driver.find_element(*LocatorsOrderPageWhoIsTheScooter.field_metro_station_form_who_is_the_scooter).click()
        self.driver.find_element(*LocatorsOrderPageWhoIsTheScooter.station_metro_form_who_is_the_scooter).click()
        self.driver.find_element(*LocatorsOrderPageWhoIsTheScooter.telephone_form_who_is_the_scooter_for).send_keys(telephone)
