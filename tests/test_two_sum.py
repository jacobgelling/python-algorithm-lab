from collections.abc import Callable

import pytest

from python_algorithm_lab.two_sum import (
    two_sum_brute_force,
    two_sum_hash_map,
)


@pytest.mark.parametrize(
    "solution",
    [two_sum_brute_force, two_sum_hash_map],
)
@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(
    solution: Callable[[list[int], int], list[int]],
    nums: list[int],
    target: int,
    expected: list[int],
) -> None:
    assert sorted(solution(nums, target)) == sorted(expected)
