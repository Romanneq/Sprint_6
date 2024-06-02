from locators.locators_order_scooter_form_about_rent import LocatorsOrderPageAboutRent
from helpers import fake_comment
from pages.BasePage import BasePage
from locators.locators_order_scooter_form_who_is_the_scooter import LocatorsOrderPageWhoIsTheScooter
import allure



class OrderPageAboutRent(BasePage): # Создали класс формы заказа самоката: "Про аренду?"

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод заполнения формы "Про аренду"')
    def completion_form_about_rent(self):
        super().click_element_page(LocatorsOrderPageWhoIsTheScooter.button_go_to_rental_form)
        super().wait_element_page(LocatorsOrderPageAboutRent.text_form_about_rent)
        super().click_element_page(LocatorsOrderPageAboutRent.field_when_to_bring_the_scooter)
        super().wait_element_page(LocatorsOrderPageAboutRent.date_picker)
        super().click_element_page(LocatorsOrderPageAboutRent.date_on_calendar)
        super().click_element_page(LocatorsOrderPageAboutRent.field_rental_period)
        super().wait_element_page(LocatorsOrderPageAboutRent.drop_down_menu_rental_period)
        super().click_element_page(LocatorsOrderPageAboutRent.rental_period_selection_list)
        super().click_element_page(LocatorsOrderPageAboutRent.color_scooter_black)
        fake = fake_comment()
        super().send_keys_element(LocatorsOrderPageAboutRent.locator_comment, fake)
        super().click_element_page(LocatorsOrderPageAboutRent.button_order_form_about_rent)
        super().wait_element_page(LocatorsOrderPageAboutRent.window_order_confirm)
        super().click_element_page(LocatorsOrderPageAboutRent.button_yes)
        super().wait_element_page(LocatorsOrderPageAboutRent.order_status_window)
    @allure.step('Метод отображения статуса заказа"')
    def display_order_status(self):
        return super().display_element_page(LocatorsOrderPageAboutRent.order_status_window)