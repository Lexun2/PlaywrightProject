from pom import LoginPage, DashboardPage
import pytest, re, allure

@allure.feature('Тест авторизации')
@allure.story('Login Feature')
@allure.title("Негативный тест авторизации")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('username, password, result', [
                        ("123","admin", "Invalid credentials. Please try again."),
                        ("admin","nhy", "Invalid credentials. Please try again."),
                        ("rty","vr4r", "Invalid credentials. Please try again."),
                                                ])
def test_login_failure(login_page, username, password, result):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step("Шаг 1. Вводим ложные логин/пароль"):
        login_page.login(username, password)
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == result
"""как дела ослики"""


"""Как дела бездельники"""
@allure.feature('Login')
@allure.story('Login Feature')
@allure.title("Позитивный тест авторизации")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('username, password', [
                        ("admin","admin",),
                        ("user","user"),
                                                ])
def test_login_success(login_page, dashboard_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step("Шаг 1. Вводим верные логин/пароль"):
        login_page.login(username, password)
    with allure.step('Переход на страницу Дашборда.'):
        dashboard_page.assert_welcome_message(f"Welcome {username}")