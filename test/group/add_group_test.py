__author__ = 'Teo'
from model.group_data import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*7
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata=[
             Group(name='Best friends', header='My best friends', footer='Hell yeah'),
             Group(name=" ", header=" ", footer=" "),
             Group("", "", "")
         ] + \
         [Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
          for i in range(5)]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    app.group.prepare_group_test_suite()
    old_groups = app.group.get_all_groups()
    app.group.create(group)
    # Count groups
    assert len(old_groups) + 1 == app.group.count()
    # Check groups list
    new_groups = app.group.get_all_groups()
    old_groups.append(group)
    app.group.check_if_groups_are_equal(old_groups, new_groups)
