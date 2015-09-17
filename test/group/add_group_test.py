__author__ = 'Teo'


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    app.group.prepare_group_test_suite()
    old_groups = db.get_group_list()
    app.group.create(group)
    # Check groups list
    new_groups = db.get_group_list()
    old_groups.append(group)
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)
