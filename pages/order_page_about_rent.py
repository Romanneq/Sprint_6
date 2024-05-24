from locators.locators_order_scooter_form_about_rent import LocatorsOrderPageAboutRent
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import fake_comment



class OrderPageAboutRent: # Создали класс формы заказа самоката: "Про аренду?"

    def __init__(self, driver):
        self.driver = driver

    def completion_form_about_rent(self): # Метод заполнения формы "Про аренду"
        self.driver.find_element(*LocatorsOrderPageAboutRent.field_when_to_bring_the_scooter).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPageAboutRent.date_picker))
        self.driver.find_element(*LocatorsOrderPageAboutRent.date_on_calendar).click()
        self.driver.find_element(*LocatorsOrderPageAboutRent.field_rental_period).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPageAboutRent.drop_down_menu_rental_period))
        self.driver.find_element(*LocatorsOrderPageAboutRent.rental_period_selection_list).click()
        self.driver.find_element(*LocatorsOrderPageAboutRent.color_scooter_black).click()
        fake = fake_comment() # генерация фейкового комментария
        self.driver.find_element(*LocatorsOrderPageAboutRent.locator_comment).send_keys(fake)
        self.driver.find_element(*LocatorsOrderPageAboutRent.button_order_form_about_rent).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPageAboutRent.window_order_confirm))
        self.driver.find_element(*LocatorsOrderPageAboutRent.button_yes).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPageAboutRent.order_status_window))


