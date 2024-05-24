import allure
import data
from selenium import webdriver
from locators.locators_main_page import LocatorsMainPage
from locators.locators_main_page import LocatorsDzen
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestLogoYandex:

    driver = None
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка логотипа, клик по Яндекс')
    def test_logo_yandex_yandex(self):
        self.driver.get(data.URL)
        self.driver.find_element(*LocatorsMainPage.logo_yandex_yandex).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsDzen.logo_yandex_dzen))
        assert self.driver.find_element(*LocatorsDzen.logo_yandex_dzen).is_displayed()

    @allure.title('Проверка логотипа, клик по Самокат')
    def test_logo_yandex_samokat(self):
        self.driver.get(data.URL)
        self.driver.find_element(*LocatorsMainPage.logo_yandex_samokat).click()
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(LocatorsMainPage.locator_main_page))
        assert self.driver.find_element(*LocatorsMainPage.locator_main_page).is_displayed()

    @classmethod
    def teardown_class(cls):
        # закрыли браузер Firefox
        cls.driver.quit()
