__author__ = 'Teo'
from sys import maxsize


class Group:

    def __init__(self, name, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        if self.check_two_fields(self.name, other.name):
            if self.id is None or other.id is None or self.id == other.id:
                return True
        return False

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def check_two_fields(self, first_field, second_field):
        if (first_field == second_field) or\
                (first_field == "" and second_field == " ") or\
                (first_field == " " and second_field == ""):
            return True
        return False