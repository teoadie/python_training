__author__ = 'Teo'


def delete_all_contacts(app):
    app.session.login_as_admin()
    app.contact.delete_first_contact()
    app.session.logout()

def test_delete_first_contact(app):
    app.session.login_as_admin()
    app.contact.delete_first_contact()
    app.session.logout()
