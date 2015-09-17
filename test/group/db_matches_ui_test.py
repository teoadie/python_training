__author__ = 'Teo'
from model.group_data import Group


def test_group_list(app, db):
    groups_from_web = app.group.get_all_groups()

    def clear(group):
        return Group(id=group.id, name=group.name.strip())
    groups_from_db = map(clear, db.get_group_list())
    assert sorted(groups_from_web, key=Group.id_or_max) == sorted(groups_from_db, key=Group.id_or_max)
