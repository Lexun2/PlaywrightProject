import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
      
        "viewport": {
            "width": 1600,
            "height": 800,
        }
    }

# @pytest.fixture(scope="session")
# def page(page):
#     return {
#       **page
#       }


from pom import LoginPage
from pom import DashboardPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)