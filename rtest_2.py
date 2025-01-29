import os
import pathlib
import re
import asyncio
import pytest, datetime
from playwright.sync_api import Playwright, sync_playwright, expect

# @pytest.fixture()
# def browser_context_args(browser_context_args):
# return {

# "http_credentials": {
# "username": "admin",
# "password": "Йцукен",
# }
# }


# def test_checkbox(page):
#     page.goto('https://zimaev.github.io/checks-radios/')
#     page.locator("text=Default checkbox").check()
#     page.locator("text=Checked checkbox").click()
#     page.locator("text=Default radio").check()
#     page.locator("text=Default checked radio").click()
#     page.locator("text=Checked switch checkbox input").click()

# def test_select(page):
#     page.goto('https://zimaev.github.io/select/')
#     page.select_option('#skills', value=["playwright", "python"])
#     page.select_option('#floatingSelect', value="3")
#     page.select_option('#floatingSelect', index=1)
#     page.select_option('#floatingSelect', label="Нашел и завел bug")

# def test_drag_and_drop(page):
#     page.goto('https://zimaev.github.io/draganddrop/')
#     page.drag_and_drop("#drag", "#drop")

# def test_dialogs(page):
#     page.goto("https://zimaev.github.io/dialog/")
#     page.get_by_text("Диалог Alert").click()
#     page.on("dialog", lambda dialog: dialog.accept())
#     page.get_by_text("Диалог Confirmation").click()
#     # dialog.accept() - закрыть диалоговое окно нажав кнопку «OK»
#     # dialog.accept("value") - чтобы вписать значение
#     # dialog.default_value - возвращает значение подсказки по умолчанию, в случае если тип диалога prompt
#     # dialog.dismiss() - закрыть диалоговое окно нажав кнопку «Отмена/Cancel»
#     # dialog.message - возвращает сообщение отображаемое в диалоговом окне.
#     # dialog.type - возвращает тип диалогового окна
#     page.get_by_text("Диалог Prompt").click()   

# def test_select_multiple(page):
#     page.goto('https://zimaev.github.io/upload/')
#     page.set_input_files("#formFile", os.path.abspath(pathlib.Path('ppp.txt')))
#     # page.set_input_files("#formFile",'ppp.txt')
#     page.locator("#file-submit").click()

# def test_download(page):
#     page.goto("https://demoqa.com/upload-download", timeout =50000.00, wait_until ="domcontentloaded")
#     page.wait_for_selector("a:has-text(\"Download\")")
#     with page.expect_download() as download_info:
#         page.locator("a:has-text(\"Download\")").click()
#     download = download_info.value
#     # download.cancel() - отменяет загрузку
#     # download.delete() - удаляет загруженный файл
#     # download.failure() - возвращает ошибку загрузки, если таковая имеется.
#     # download.page - возвращает объект страницы, к которой принадлежит загрузка.
#     # download.path() - возвращает путь к загруженному файлу
#     # download.save_as(path) - скопирует загруженный файл по указанному пути
#     # download.suggested_filename - возвращает имя файла
#     # download.url - возвращает загруженный URL-адрес
#     file_name = download.suggested_filename
#     destination_folder_path = "./data/"
#     download.save_as(os.path.join(destination_folder_path, file_name))

# def test_inner(page):
#     page.goto('https://zimaev.github.io/table/')
#     element = page.locator('tr:has-text("Thornton")')
#     print(element.inner_html())
#     print("\n")
#     row = page.locator("td")
#     print(row.all_inner_texts())
#     print("\n")
#     row = page.locator("tr")
#     print(row.all_inner_texts())
#     print("\n")
#     row = page.locator("tr")
#     print(row.all_text_contents())
    

# def test_screenshots(page):
#     page.goto('https://dzen.ru/')
#     # Параметры type="jpeg"|"png", full_page=True|False, quality = Качество сжатия изображения для формата 'jpeg'(0-100), 
#     # clip (dict): Задает область для создания скриншота, указав координаты x, y, ширину и высоту.
#     # omit_background (bool): Позволяет убрать фон изображения. Если True, фон на скриншоте будет прозрачным, что актуально в случае формата 'png'. По умолчанию значение False.
#     # timeout (float | int): Задает максимальное время ожидания (в миллисекундах) перед созданием скриншота. По умолчанию 30000 миллисекунд (30 секунд).
#     # скриншот страницы
#     page.screenshot(path="screenshot1.png")
#     # скриншот всей страницы (скриншот всей страницы (True) или только видимой области (False-дефолт))
#     page.screenshot(path="screenshot2.png", full_page=False, type="jpeg", quality=50, clip={"x": 50, "y": 0, "width": 400, "height": 300}, omit_background=False, timeout=10000)
#     # скриншот элемента
#     page.locator("#dzen-header > div.dzen-layout--desktop-base-header__logoContainer-pu.dzen-layout--desktop-base-header__isMorda-2n > a > svg.dzen-layout--desktop-base-header__logo-2H.dzen-layout--desktop-base-header__isMorda-2n").screenshot(path="screenshot3.png")



# если в тесте открывается новая вкадка, то для новой нужен новый экземплр объекта page
def test_new_tab(page):
    page.goto("https://zimaev.github.io/tabs/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()
    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()
# Метод page.context.expect_page()  ожидает открытия новой вкладки. Переменная tab - это класс EventInfo, возвращаемый менеджером контекста with. Мы можем получить доступ к классу с помощью свойства value.


