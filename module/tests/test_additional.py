from module import con


def test_correct_data():
    assert con.additional() == (1, [])
