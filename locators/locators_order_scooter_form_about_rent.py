from selenium.webdriver.common.by import By



class LocatorsOrderPageAboutRent:
    text_form_about_rent = [By.XPATH, ".//div[text() = 'Про аренду']"] # локатор формы "Про самокат"
    field_when_to_bring_the_scooter = [By.XPATH, ".//div[@class='react-datepicker__input-container']"] # локатор поля "Когда привезти самокат?"
    date_picker = [By.XPATH, ".//div[@class='react-datepicker-popper']"] # локатор выпадающего календаря при клике на поле "Когда привезти самокат?"
    date_on_calendar = [By.XPATH, ".//div[contains(@class, 'react-datepicker__day--keyboard-selected react-datepicker__day--today')]/following-sibling::div[1]"] # локатор завтрашней даты в раскрывающемся календаре
    field_rental_period = [By.XPATH, ".//div[@class='Dropdown-root']"] # локатор поля срок аренды
    drop_down_menu_rental_period = [By.XPATH, ".//div[@class='Dropdown-menu']"] # локатор выпадающего списка срока аренды
    rental_period_selection_list = [By.XPATH, ".//div[text()='сутки']"] # локатор "сутки" в выпадающем списке
    color_scooter_black = [By.XPATH,".//input[@id = 'black']"] # локатор чек-бокса "Черный жемчуг"
    locator_comment = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"] # локатор поля "Комментарий для курьера"
    button_order_form_about_rent = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']//child::button[text()='Заказать']"] # локатор кнопки "Заказать"
    window_order_confirm = [By.XPATH, ".//div[text()='Хотите оформить заказ?']"] # локатор формы подтверждения заказа
    button_yes = [By.XPATH, ".//button[text()='Да']"] # локатор кнопки "Да"
    order_status_window = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']"] # локатор отображения статуса заказа