import pytest
from main import check_diff_info_in_lists


@pytest.mark.parametrize('list1, list2, result', [
    (["vova", "maksym", "artem", "ivan"], ["artem", "ivan", "nastya", "igor"], ["vova", "maksym"]),
    ([5, 8, 1, 3], [1, 8, 3, 6], [5]),
    ([1, 2, 3, 4, 8], [3, 2, 1, 5, 7], [4, 8])
])
def test_check_diff_info(list1, list2, result):
    check = check_diff_info_in_lists(list1, list2)
    assert check == result
