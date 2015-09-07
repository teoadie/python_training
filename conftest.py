__author__ = 'Teo'
from fixture.application import Application
import pytest


fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login_as_admin()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fixture_teardown():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fixture_teardown)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")