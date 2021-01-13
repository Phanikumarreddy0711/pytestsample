from school.parent import parent
from school.student import student
import pytest


def test_construction():
    s = student('Phani', 'Kumar')
    assert 'Phani' == s.first_name
    assert 'Kumar' == s.last_name
    assert [] == s.parents


def test_add_parent():
    p = parent('Mary', 'Jones')
    s = student('Phani', 'Kumar')
    s.add_parent(p)
    assert [p] == s.parents


# @pytest.mark.skip(reason='have not yet implemented method')
def test_add_parents():
    s = student('phani', 'kumar')
    p1 = parent('Mary', 'Jones')
    s.add_parent(p1)
    p2 = parent('Jani', 'Papa')
    p3 = parent('Suri', 'Jonson')
    s.add_parents((p2, p3))
    assert [p1, p2, p3] == s.parents


# @pytest.mark.skip(reason='have not yet implemented method')
def test_primary_parent():
    s = student('phani', 'kumar')
    p1 = parent('Mary', 'Jones')
    s.add_parent(p1)
    p2 = parent('Jani', 'Papa')
    p3 = parent('Suri', 'Jonson')
    s.add_parents((p2, p3))
    assert [p1, p2, p3] == s.parents
