import pytest
from main import check_same_info_in_lists


@pytest.mark.parametrize('list1, list2, result', [
    (["vova", "maksym", "artem", "ivan"], ["artem", "ivan", "nastya", "igor"], ["artem", "ivan"]),
    ([5, 8, 1, 3], [1, 8, 3, 6], [8, 1, 3]),
    ([1, 2, 3, 4], [3, 2, 1, 5, 7], [1, 2, 3])
])
def test_check_same_info_in_lists(list1, list2, result):
    check = check_same_info_in_lists(list1, list2)
    assert check == result
