from module import con
import pytest


@pytest.fixture()
def temp():
    return ['D6', 'A2']


def test_count(temp):
    assert con.count(*temp) == (3, 2)
