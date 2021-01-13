from school.parent import parent
def test_construction():
    p = parent('Marry', 'Jones')
    assert 'Marry' == p.first_name
    assert 'Jones' == p.last_name