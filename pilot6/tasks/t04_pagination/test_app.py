import pytest
from app import page_count

@pytest.mark.parametrize('total,size,expected', [
    (0,10,0),(1,10,1),(9,10,1),(10,10,1),(11,10,2),(20,10,2),(21,10,3)
], ids=['empty','single','partial','exact','one-over','two-exact','two-plus-one'])
def test_page_count(total,size,expected):
    assert page_count(total,size) == expected

@pytest.mark.parametrize('total,size', [(-1,10),(1,0),(1,-1)])
def test_invalid(total,size):
    with pytest.raises(ValueError):
        page_count(total,size)
