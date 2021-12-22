from module import con


def test_correct_data():
    con.additional()
    assert con.move(4, 6) == ['43', '52', '45', '56', '76', '85', '83', '72']