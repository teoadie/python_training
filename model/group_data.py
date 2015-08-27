__author__ = 'Teo'
from sys import maxsize


class Group:

    def __init__(self, name, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        if self.name == other.name:
            if self.id is None or other.id is None or self.id == other.id:
                return True
        return False

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
