import pytest


def test_example_1():
    assert 1+1 == 2

@pytest.mark.second
def test_2():
    assert len('ho') == 2