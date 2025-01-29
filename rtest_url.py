from playwright.sync_api import Playwright, sync_playwright, expect, Route
import re

# def test_todo(page):
#     page.goto('https://demo.playwright.dev/todomvc/#/')
#     expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
#     input_element = page.get_by_placeholder("What needs to be done?")
#     expect(input_element).to_be_empty()
#     input_element.fill("Хочу стать AQA")
#     input_element.press("Enter")
#     todo_item = page.get_by_test_id('todo-item')
#     expect(todo_item).to_have_count(1)
#     input_element.fill("Хочу стать AQA2")
#     input_element.press("Enter")
#     expect(todo_item).to_have_count(3)
#     input_element.fill("Хочу стать AQA3")
#     input_element.press("Enter")
#     expect(todo_item).to_have_count(3)
#     todo_item.get_by_role('checkbox').nth(1).click()
#     expect(todo_item.nth(1)).to_have_class("completed")
#     # page.pause() 
#     # page.wait_for_timeout(3000)

# def test_listen_network(page):
#     # page.on("request", lambda request: print(">>", request.method, request.url))
#     # page.on("response", lambda response: print("<<", response.status, response.url))
#     page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
#     page.goto('https://ya.ru/')
#     page.pause()

# def test_network(page):
#     page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
#     page.on("response", lambda response: print("<<", response.status, response.url))
#     page.goto('https://reqres.in/')
#     page.get_by_text(' Register - successful ').click()
#     page.pause()

# def test_mock_tags(page):
#     # page.route("**/search/?text=%D0%BE%D0%B7%D0%BE%D0%BD&lr=1", lambda route: route.continue_("**/search/?text=вайлдберис&lr=1"))
#     # page.route('https://www.yandex.ru/search/?text=%D0%BE%D0%B7%D0%BE%D0%BD&lr=1')

#     page.route(re.compile(r"((facebook)|(twitter)|(google))"),  lambda route: route.fulfill(status=404, content_type="text/plain"))
#     page.goto('https://www.facebook.ru')
#     page.pause()


# def test_intercepted(page):
#     def handle_route(route: Route):
#         response = route.fetch()
#         json = response.json()
#         json["tags"] = ["open", "solutions"]
#         route.fulfill(json=json)

#     page.route("**/api/tags", handle_route)

#     page.goto("https://demo.realworld.io/")
#     sidebar = page.locator('css=div.sidebar') 
#     expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])

# def test_intercepted(page):
#     def handle_route(route: Route):
#         response = route.fetch()
#         json = response.json()
#         print(json.keys())
#         # json["tags"] = ["open", "solutions"]
#         # route.fulfill(json=json)
#         route.continue_()

#     page.route("https://www.yandex.ru/search/?text=mama", handle_route)
#     page.goto("https://www.yandex.ru/search/?text=mama")
#     page.pause()
#     # sidebar = page.locator('css=div.sidebar') 
#     # expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])

# def test_replace_from_har(page):
#     page.goto("https://reqres.in/", timeout=100000)
#     page.route_from_har("example.har")
#     users_single = page.locator('li[data-id="users-single"]')
#     users_single.click()
#     response = page.locator('[data-key="output-response"]')
#     page.pause()


def test_inventory(page):
    # page.set_extra_http_headers({"Authorization": "Bearer <token>"})
    # response = page.request.get("https://example.com/")
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(response.status)
    print(response.json())

def test_add_user(page):
    data = [
              {
                "id": 9743,
                "username": "lex",
                "firstName": "alex",
                "lastName": "xela",
                "email": "bbb@rr",
                "password": "ytt",
                "phone": "3343",
                "userStatus": 0
              }
            ]
    header = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray',data=data, headers=header)
    print(response.status)
    print(response.json())
    print(response.body())