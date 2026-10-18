import pytest

from python_algorithm_lab.add_two_numbers import add_two_numbers
from python_algorithm_lab.add_two_numbers import ListNode


@pytest.mark.parametrize(
    ("l1", "l2", "expected"),
    [
        (
            ListNode(2, ListNode(4, ListNode(3))),
            ListNode(5, ListNode(6, ListNode(4))),
            ListNode(7, ListNode(0, ListNode(8))),
        ),
        (
            ListNode(0),
            ListNode(0),
            ListNode(0),
        ),
        (
            ListNode(
                9,
                ListNode(
                    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
                ),
            ),
            ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
            ListNode(
                8,
                ListNode(
                    9,
                    ListNode(
                        9,
                        ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))),
                    ),
                ),
            ),
        ),
    ],
)
def test_two_sum(
    l1: ListNode | None,
    l2: ListNode | None,
    expected: ListNode | None,
) -> None:
    result = add_two_numbers(l1, l2)

    while result or expected:
        assert result.val == expected.val
        result = result.next if result else None
        expected = expected.next if result else None

    assert result is None
    assert expected is None
