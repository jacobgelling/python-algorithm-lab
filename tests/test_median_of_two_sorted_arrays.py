from collections.abc import Callable

import pytest

from python_algorithm_lab.median_of_two_sorted_arrays import (
    find_median_sorted_arrays_easy,
)
from python_algorithm_lab.median_of_two_sorted_arrays import (
    find_median_sorted_arrays_merge_sort,
)


@pytest.mark.parametrize(
    "solution",
    [
        find_median_sorted_arrays_easy,
        find_median_sorted_arrays_merge_sort,
    ],
)
@pytest.mark.parametrize(
    ("nums1", "nums2", "expected"),
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
    ],
)
def test_find_median_of_two_sorted_arrays(
    solution: Callable[[list[int], list[int]], float],
    nums1: list[int],
    nums2: list[int],
    expected: float,
) -> None:
    assert solution(nums1, nums2) == expected
