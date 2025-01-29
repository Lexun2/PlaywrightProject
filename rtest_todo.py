import re
import asyncio
import pytest, datetime
from playwright.sync_api import Playwright, sync_playwright, expect




# class TestExample:
def test_add_todo(page):
    

    page.goto("https://w140.zona.plus/")
    page.get_by_role("link", name="Фильмы", exact=True).click()
    page.locator('//*[@id="filter-id-genreId"]').click()
    page.select_option('//*[@id="filter-id-genreId"]', label='приключения')
    # page.locator("#filter-id-genreId >> option:has-text('приключения')").click()
    page.locator('//*[@id="filter-id-year"]').click()
    page.select_option('//*[@id="filter-id-year"]', label='2024')
    # page.locator(".results > .results-item > .result-item-footer > .results-item-title").all()
    # films = page.locator(".results-item-title").all()
    # text2=""
    # for li in films[0:10]:
    #         text = li.inner_text()
    #         print(text)
    #         text2=text2+text+"\n"
    page.get_by_role("link", name="Огниво").click()
    actors = page.locator(".entity-desc-value >> span:has-text('Роман Евдокимов')").first
    print(actors.inner_text())

    name = page.locator("span").filter(has_text="Евдокимов").first
    print("Актёр - "+name.inner_text())

    date = page.locator(".entity-desc-item-wrap").filter(has_text="Премьера")
    date_final=date.locator("span").inner_text()
    print(re.match(r'\d\d\s.*\d\d\d\d',date_final).group(0)) 


    fil = page.locator("span")
    for a in fil.all():
        print(a.inner_text())
    
    print("imdb = ",fil.filter(has = page.locator(".entity-rating-imdb")).inner_text())

    page.wait_for_timeout(1000)


    # page.locator('//*[@title="Огниво"]').click()

    # a.locator("a").click()
    # page.locator("li >> .results-item").filter(has_text='Красный').click()

  
    # print(page.locator(".results > .results-item-wrap").inner_text())



    # page.wait_for_selector('div#my-element', state='visible')
    #filter-id-genreId > option:nth-child(9)
    # //*[@id="filter-id-genreId"]/option[9]
    # page.locator('#filter-id-genreId > option:nth-child(9)').click(force=True)



    #filter-id-genreId > option:nth-child(9)
    
    # logo_text=page.locator(".text-mute").inner_text()
        # logo_text=page.locator('p:has-text("hunington@gmail")').inner_text()
        # print(f"{logo_text} вот её почта")
    
    # page.get_by_placeholder("What needs to be done?").click()
    # page.get_by_placeholder("What needs to be done?").fill("Привет")
    # page.get_by_placeholder("What needs to be done?").press("Enter")
    # page.get_by_placeholder("What needs to be done?").fill("Медвед")
    # page.get_by_placeholder("What needs to be done?").press("Enter")
        # date = datetime.datetime.now().strftime('%d-%m-%y_%H-%M-%S-%f')
        # page.screenshot(path=f"{date}.png")
    # page.locator('button:has-text("Log in"), button:has-text("Sign in")').click()
        
    # @pytest.mark.skip_browser("firefox")
    # @pytest.mark.only_browser("chromium")
    # def test_add_todo2(self, page):
    #     page.goto("https://demo.playwright.dev/todomvc/#/")
    #     page.get_by_placeholder("What needs to be done?").click()
    #     page.get_by_placeholder("What needs to be done?").fill("Привет")
    #     page.get_by_placeholder("What needs to be done?").press("Enter")
    #     page.get_by_placeholder("What needs to be done?").fill("Медвед")
    #     page.get_by_placeholder("What needs to be done?").press("Enter")  
