__author__ = 'Teo'
from fixture.application import Application
import pytest


fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
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
