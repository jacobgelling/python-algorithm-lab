from collections.abc import Callable

import pytest

from python_algorithm_lab.longest_substring_without_repeating_characters import (
    length_of_longest_substring_brute_force,
)
from python_algorithm_lab.longest_substring_without_repeating_characters import (
    length_of_longest_substring_sliding_window,
)


@pytest.mark.parametrize(
    "solution",
    [
        length_of_longest_substring_brute_force,
        length_of_longest_substring_sliding_window,
    ],
)
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_length_of_longest_substring(
    solution: Callable[[str], int], s: str, expected: int
) -> None:
    assert solution(s) == expected
