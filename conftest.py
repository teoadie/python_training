__author__ = 'Teo'
from fixture.application import Application
from fixture.orm import ORMFixture
import pytest
import jsonpickle
import json
import os.path
import importlib

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file_path) as config_file:
            target = json.load(config_file)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
        fixture.set_default_user(web_config["userName"], web_config["userPassword"])
    fixture.session.ensure_login_by_default_user()
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = ORMFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                          password=db_config["password"])
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fixture_teardown():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fixture_teardown)


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        if fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as json_file:
        return jsonpickle.decode(json_file.read())
