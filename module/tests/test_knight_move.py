from module.con import knight_move


def test_correct_data():
    assert knight_move((4, 6), 'A2') == 3
