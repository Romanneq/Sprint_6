# Проект автоматизации тестирования сервиса Яндекс.Самокат

1. Ссылка на сервис: "https://qa-scooter.praktikum-services.ru/"
2. Основа для написания автотестов — фреймворк selenium.
3. Установить зависимости — pip3 install -r requirements.txt (# Если более ранняя версия Python, вместо pip3, использовать pip)
4. Проверить, что selenium, pytest, allure, faker установлены: pip freeze
5. Команда для запуска — run
6. Описания локаторов – в директории locators
7. Генерация данных для регистрации - в файле helpers.py
8. Запустить allure отчет: allure serve allure_results