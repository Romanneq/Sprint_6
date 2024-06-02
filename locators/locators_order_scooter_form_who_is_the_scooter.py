from selenium.webdriver.common.by import By



class LocatorsOrderPageWhoIsTheScooter:
    text_form_who_is_the_scooter_for = [By.XPATH,'.//div[contains(@class,"Order_Header__")]'] # локатор текста формы "Для кого самокат?"
    first_name_form_who_is_the_scooter = [By.XPATH, './/input[@placeholder = "* Имя"]'] # локатор поля Имя в форме "Для кого самокат?"
    second_name_form_who_is_the_scooter = [By.XPATH, './/input[@placeholder = "* Фамилия"]'] # локатор поля Фамилия в форме "Для кого самокат?"
    address_form_who_is_the_scooter = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"] # локатор поля Адрес в форме "Для кого самокат?"
    field_metro_station_form_who_is_the_scooter = [By.XPATH, ".//input[@class = 'select-search__input']"] # локатор поля Станция метро в форме "Для кого самокат?
    station_metro_form_who_is_the_scooter = [By.XPATH, '//li[@data-value="1"]'] # локатор первой станции в раскрывающемся списке Станций метро в форме "Для кого самокат?"
    telephone_form_who_is_the_scooter_for = [By.XPATH, ".//input[@placeholder ='* Телефон: на него позвонит курьер']"] # локатор поля Телефон в форме "Для кого самокат?
    button_go_to_rental_form = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__')]"] # кнопка "Далее" в форме "Для кого самокат"



