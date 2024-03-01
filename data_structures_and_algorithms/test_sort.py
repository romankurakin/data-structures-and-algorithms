import pytest
from sort import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

sort_functions = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


@pytest.mark.parametrize("sort_func", sort_functions)
def test_empty_list(sort_func):
    arr = []
    assert sort_func(arr) == []


@pytest.mark.parametrize("sort_func", sort_functions)
def test_single_element(sort_func):
    arr = [5]
    assert sort_func(arr) == [5]


@pytest.mark.parametrize("sort_func", sort_functions)
def test_ascending_order(sort_func):
    arr = [1, 2, 3, 4, 5]
    assert sort_func(arr) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("sort_func", sort_functions)
def test_descending_order(sort_func):
    arr = [5, 4, 3, 2, 1]
    assert sort_func(arr) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("sort_func", sort_functions)
def test_random_order(sort_func):
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = sort_func(arr)
    assert is_sorted(sorted_arr)


@pytest.mark.parametrize("sort_func", sort_functions)
def test_large_list(sort_func):
    arr = list(range(100, 0, -1))
    sorted_arr = sort_func(arr)
    assert is_sorted(sorted_arr)


@pytest.mark.parametrize("sort_func", sort_functions)
def test_duplicate_elements(sort_func):
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = sort_func(arr)
    assert is_sorted(sorted_arr)
