import allure
from selenium import webdriver
from pages.main_page import MainPageSamokat
import data
import pytest
from locators.locators_main_page import QuestionsAboutImportantOnMainPage



class TestQuestionsAboutImportant:

    driver = None
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка вопроса: "Сколько это стоит? И как оплатить?"')
    @pytest.mark.parametrize('text_a', ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.'])
    def test_questions_1(self, text_a):
        self.driver.get(data.URL)
        main_page = MainPageSamokat(self.driver)
        main_page.scroll_main_page()
        self.driver.find_element(*QuestionsAboutImportantOnMainPage.questions_1).click()
        assert self.driver.find_element(*QuestionsAboutImportantOnMainPage.answer_to_the_question_1).text == text_a

    @allure.title('Проверка вопроса: "Хочу сразу несколько самокатов! Так можно?"')
    @pytest.mark.parametrize('text_a', ['Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'])
    def test_questions_2(self, text_a):
        self.driver.get(data.URL)
        main_page = MainPageSamokat(self.driver)
        main_page.scroll_main_page()
        self.driver.find_element(*QuestionsAboutImportantOnMainPage.questions_2).click()
        assert self.driver.find_element(*QuestionsAboutImportantOnMainPage.answer_to_the_question_2).text == text_a

    @allure.title('Проверка вопроса: "Как рассчитывается время аренды?"')
    @pytest.mark.parametrize('text_a', ['Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'])
    def test_questions_3(self, text_a):
        self.driver.get(data.URL)
        main_page = MainPageSamokat(self.driver)
        main_page.scroll_main_page()
        self.driver.find_element(*QuestionsAboutImportantOnMainPage.questions_3).click()
        assert self.driver.find_element(*QuestionsAboutImportantOnMainPage.answer_to_the_question_3).text == text_a

    @allure.title('Проверка вопроса: "Можно ли заказать самокат прямо на сегодня?"')
    @pytest.mark.parametrize('text_a', ['Только начиная с завтрашнего дня. Но скоро станем расторопнее.'])
    def test_questions_4(self, text_a):
        self.driver.get(data.URL)
        main_page = MainPageSamokat(self.driver)
        main_page.scroll_main_page()
        self.driver.find_element(*QuestionsAboutImportantOnMainPage.questions_4).click()
        assert self.driver.find_element(*QuestionsAboutImportantOnMainPage.answer_to_the_question_4).text == text_a

    @allure.title('Проверка вопроса: "Можно ли продлить заказ или вернуть самокат раньше?"')
    @pytest.mark.parametrize('text_a', ['Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'])
    def test_questions_5(self, text_a):
        self.driver.get(data.URL)
        main_page = MainPageSamokat(self.driver)
        main_page.scroll_main_page()
        self.driver.find_element(*QuestionsAboutImportantOnMainPage.questions_5).click()
        assert self.driver.find_element(*QuestionsAboutImportantOnMainPage.answer_to_the_question_5).text == text_a

    @allure.title('Проверка вопроса: "Вы привозите зарядку вместе с самокатом?"')
    @pytest.mark.parametrize('text_a', ['Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'])
    def test_questions_6(self, text_a):
        self.driver.get(data.URL)
        main_page = MainPageSamokat(self.driver)
        main_page.scroll_main_page()
        self.driver.find_element(*QuestionsAboutImportantOnMainPage.questions_6).click()
        assert self.driver.find_element(*QuestionsAboutImportantOnMainPage.answer_to_the_question_6).text == text_a

    @allure.title('Проверка вопроса: "Можно ли отменить заказ?"')
    @pytest.mark.parametrize('text_a', ['Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'])
    def test_questions_7(self, text_a):
        self.driver.get(data.URL)
        main_page = MainPageSamokat(self.driver)
        main_page.scroll_main_page()
        self.driver.find_element(*QuestionsAboutImportantOnMainPage.questions_7).click()
        assert self.driver.find_element(*QuestionsAboutImportantOnMainPage.answer_to_the_question_7).text == text_a

    @allure.title('Проверка вопроса: "Я жизу за МКАДом, привезёте?"')
    @pytest.mark.parametrize('text_a', ['Да, обязательно. Всем самокатов! И Москве, и Московской области.'])
    def test_questions_8(self, text_a):
        self.driver.get(data.URL)
        main_page = MainPageSamokat(self.driver)
        main_page.scroll_main_page()
        self.driver.find_element(*QuestionsAboutImportantOnMainPage.questions_8).click()
        assert self.driver.find_element(*QuestionsAboutImportantOnMainPage.answer_to_the_question_8).text == text_a

    @classmethod
    def teardown_class(cls):
        # закрыли браузер Firefox
        cls.driver.quit()
