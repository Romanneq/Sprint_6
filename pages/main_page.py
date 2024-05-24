from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_main_page import LocatorsMainPage
from locators.locators_order_scooter_form_who_is_the_scooter import LocatorsOrderPageWhoIsTheScooter



class MainPageSamokat: # Создали класс главной страницы cервиса

    def __init__(self, driver):
        self.driver = driver

    def scroll_main_page(self): # метод скролла до футера страницы "Вопросы о важном"
        element = self.driver.find_element(*LocatorsMainPage.text_footer)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((LocatorsMainPage.text_footer)))

    def click_on_button_order_in_header_page(self): # метод клика на кнопку "Заказать" в заголовке страницы
        self.driver.find_element(*LocatorsMainPage.button_order_in_header).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPageWhoIsTheScooter.text_form_who_is_the_scooter_for))

    def click_on_button_order_in_work_area_page(self): # метод клика на кнопку "Заказать" в рабочей области страницы
        element = self.driver.find_element(*LocatorsMainPage.button_order_in_work_area)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsMainPage.button_order_in_work_area))
        self.driver.find_element(*LocatorsMainPage.button_order_in_work_area).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPageWhoIsTheScooter.text_form_who_is_the_scooter_for))
