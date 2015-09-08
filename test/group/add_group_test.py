__author__ = 'Teo'


def test_add_group(app, json_groups):
    group = json_groups
    app.group.prepare_group_test_suite()
    old_groups = app.group.get_all_groups()
    app.group.create(group)
    # Count groups
    assert len(old_groups) + 1 == app.group.count()
    # Check groups list
    new_groups = app.group.get_all_groups()
    old_groups.append(group)
    app.group.check_if_groups_are_equal(old_groups, new_groups)
