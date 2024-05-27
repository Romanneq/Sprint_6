import allure
from selenium import webdriver
from pages.main_page import MainPageSamokat
import pytest
from locators.locators_main_page import QuestionsAboutImportantOnMainPage



class TestQuestionsAboutImportant:

    driver = None
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка ответов "Вопросы о важном"')
    @pytest.mark.parametrize('obj_q, obj_a, text_a', [[QuestionsAboutImportantOnMainPage.questions_1, QuestionsAboutImportantOnMainPage.answer_to_the_question_1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                                                      [QuestionsAboutImportantOnMainPage.questions_2, QuestionsAboutImportantOnMainPage.answer_to_the_question_2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                                                      [QuestionsAboutImportantOnMainPage.questions_3, QuestionsAboutImportantOnMainPage.answer_to_the_question_3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                                                      [QuestionsAboutImportantOnMainPage.questions_4, QuestionsAboutImportantOnMainPage.answer_to_the_question_4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                                                      [QuestionsAboutImportantOnMainPage.questions_5, QuestionsAboutImportantOnMainPage.answer_to_the_question_5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                                                      [QuestionsAboutImportantOnMainPage.questions_6, QuestionsAboutImportantOnMainPage.answer_to_the_question_6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                                                      [QuestionsAboutImportantOnMainPage.questions_7, QuestionsAboutImportantOnMainPage.answer_to_the_question_7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                                                      [QuestionsAboutImportantOnMainPage.questions_8, QuestionsAboutImportantOnMainPage.answer_to_the_question_8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']])
    def test_questions(self, obj_q, obj_a, text_a):
        main_page_obj = MainPageSamokat(self.driver)
        assert main_page_obj.click_and_found_text(obj_q, obj_a) == text_a

    @classmethod
    def teardown_class(cls):
        # закрыли браузер Firefox
        cls.driver.quit()
