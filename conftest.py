__author__ = 'Teo'
from fixture.application import Application
import pytest
import json
import os.path

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file_path) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
        fixture.set_default_user(target["userName"], target["userPassword"])
    fixture.session.ensure_login_by_default_user()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fixture_teardown():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fixture_teardown)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")