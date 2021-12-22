from module import con


def test_research():
    con.additional()
    assert con.research((4, 6)) == ['C4', 'E4', 'B5', 'F5', 'B7', 'F7', 'C8', 'E8']