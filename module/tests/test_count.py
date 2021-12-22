from module import con


def test_count():
    assert con.count('D6', 'A2') == (3, 2)