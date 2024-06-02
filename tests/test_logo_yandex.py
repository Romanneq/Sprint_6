import allure
from selenium import webdriver
from pages.main_page import MainPageSamokat
from pages.Dzen_page import DzenPage



class TestLogoYandex:

    driver = None
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка логотипа, клик по Яндекс')
    def test_logo_yandex_yandex(self):
        main_page_obj = MainPageSamokat(self.driver)
        dzen_page_obj = DzenPage(self.driver)
        main_page_obj.click_logo_yandex_yandex()
        dzen_page_obj.display_element_page_dzen()
        assert dzen_page_obj.found_element_page_dzen()

    @allure.title('Проверка логотипа, клик по Самокат')
    def test_logo_yandex_samokat(self):
        main_page_obj = MainPageSamokat(self.driver)
        main_page_obj.click_logo_yandex_samokat()
        assert main_page_obj.display_main_page()

    @classmethod
    def teardown_class(cls):
        # закрыли браузер Firefox
        cls.driver.quit()
