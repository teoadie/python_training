__author__ = 'Teo'


def test_delete_first_group(app):
    app.session.login_as_admin()
    app.group.delete_first_group()
    app.session.logout()
