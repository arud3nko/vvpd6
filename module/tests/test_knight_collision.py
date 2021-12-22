from module.con import knights_collision


def test_correct_data():
    assert knights_collision((4, 6), (1, 2)) == 2