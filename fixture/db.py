__author__ = 'Teo'
import mysql.connector
from model.group_data import Group
from model.contact_data import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.name = name
        self.host = host
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=self.host, database=self.name, user=self.user,
                                                  password=self.password)
        self.connection.autocommit = True

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (group_id, name, header, footer) = row
                group_list.append(Group(id=str(group_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (contact_id, firstname, lastname) = row
                contact_list.append(Contact(id=str(contact_id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return contact_list
