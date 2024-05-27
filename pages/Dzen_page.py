from pages.BasePage import BasePage
from locators.locator_dzen import LocatorsDzen
import allure



class DzenPage(BasePage):  # Создали класс главной страницы сайта dzen

    def __init__(self, driver):
        self.driver = driver
    @allure.step('Метод wait элемента страницы Dzen')
    def display_element_page_dzen(self):
        return super().wait_element_page(LocatorsDzen.logo_yandex_dzen)
    @allure.step('Метод поиска элемента на странице Dzen')
    def found_element_page_dzen(self):
        return super().display_element_page(LocatorsDzen.logo_yandex_dzen)


