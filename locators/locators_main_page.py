from selenium.webdriver.common.by import By



class QuestionsAboutImportantOnMainPage:
    questions_1 = [By.ID, 'accordion__heading-0']  # локатор поля вопроса: "Сколько это стоит? И как оплатить?"
    questions_2 = [By.ID, 'accordion__heading-1']  # локатор поля вопроса: "Хочу сразу несколько самокатов! Так можно?"
    questions_3 = [By.ID, 'accordion__heading-2']  # локатор поля вопроса: "Как рассчитывается время аренды?"
    questions_4 = [By.ID, 'accordion__heading-3']  # локатор поля вопроса: "Можно ли заказать самокат прямо на сегодня?"
    questions_5 = [By.ID, 'accordion__heading-4']  # локатор поля вопроса: "Можно ли продлить заказ или вернуть самокат раньше?"
    questions_6 = [By.ID, 'accordion__heading-5']  # локатор поля вопроса: "Вы привозите зарядку вместе с самокатом?"
    questions_7 = [By.ID, 'accordion__heading-6']  # локатор поля вопроса: "Можно ли отменить заказ?"
    questions_8 = [By.ID, 'accordion__heading-7']  # локатор поля вопроса: "Я жизу за МКАДом, привезёте?"
    answer_to_the_question_1 = [By.XPATH, ".//div[@id = 'accordion__panel-0']"]  # локатор ответа на вопрос: "Сколько это стоит? И как оплатить?"
    answer_to_the_question_2 = [By.XPATH, ".//div[@id = 'accordion__panel-1']"] # локатор ответа на вопрос: "Хочу сразу несколько самокатов! Так можно?"
    answer_to_the_question_3 = [By.XPATH, ".//div[@id = 'accordion__panel-2']"] # локатор ответа на вопрос: "Как рассчитывается время аренды?"
    answer_to_the_question_4 = [By.XPATH, ".//div[@id = 'accordion__panel-3']"] # локатор ответа на вопрос: "Можно ли заказать самокат прямо на сегодня?"
    answer_to_the_question_5 = [By.XPATH, ".//div[@id = 'accordion__panel-4']"] # локатор ответа на вопрос: "Можно ли продлить заказ или вернуть самокат раньше?"
    answer_to_the_question_6 = [By.XPATH, ".//div[@id = 'accordion__panel-5']"] # локатор ответа на вопрос: "Вы привозите зарядку вместе с самокатом?"
    answer_to_the_question_7 = [By.XPATH, ".//div[@id = 'accordion__panel-6']"] # локатор ответа на вопрос: "Можно ли отменить заказ?"
    answer_to_the_question_8 = [By.XPATH, ".//div[@id = 'accordion__panel-7']"] # локатор ответа на вопрос: "Я жизу за МКАДом, привезёте?"
class LocatorsMainPage:
    questions_about_important = [By.XPATH, ".//div[contains(@class, 'Home_FAQ__')]"] # Локатор формы "Вопросы о важном" в футере главной страницы
    button_order_in_header = [By.XPATH, ".//div[contains(@class, 'Header_Nav_')]/button[contains(@class, 'Button_Button__')]"] # локатор кнопки заказать в шапке страницы
    button_order_in_work_area = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"] # локатор кнопки заказать в рабочей области страницы
    logo_yandex_yandex = [By.XPATH, ".//a[contains(@class, 'Header_LogoYandex__')]"] # локатор логотипа Яндекс.Самокат (Яндекс)
    logo_yandex_samokat = [By.XPATH, './/a[contains(@class, "Header_LogoScooter__")]'] # локатор логотипа Яндекс.Самокат (Самокат)
    locator_main_page = [By.XPATH, ".//div[contains(@class, 'Home_Header__')]"] # локатор текста главной страницы: "Самокат на пару дней Привезём его прямо к вашей двери,а когда накатаетесь — заберём"
