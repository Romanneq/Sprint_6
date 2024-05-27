import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data



class BasePage: # Создали класс главной страницы cервиса
    def __init__(self, driver):
        self.driver = driver
    @allure.step('Метод отображения URL главной страницы сервиса')
    def url_page(self):
        self.driver.get(data.URL)

    @allure.step('Метод скролла страницы')
    def base_scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((locator)))

    @allure.step('Метод получения текста элемента')
    def base_text_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Метод ожидания отображения элемента')
    def wait_element_page(self, locator): # ожидание отображения элемента
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((locator)))

    @allure.step('Метод перехода на другую страницу браузера')
    def swith_another_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Метод клика по элементу страницы')
    def click_element_page(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Метод отображения элемента страницы')
    def display_element_page(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Метод ввода текста в поле элемента страницы')
    def send_keys_element(self, locator, text):
        return self.driver.find_element(*locator).send_keys(text)