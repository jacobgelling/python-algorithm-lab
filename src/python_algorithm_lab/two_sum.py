"""https://leetcode.com/problems/two-sum/"""


def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """Time: O(n²), Space: O(1)"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    raise ValueError("No solution exists")


def two_sum_hash_map(nums: list[int], target: int) -> list[int]:
    """Time: O(n), Space: O(n)"""
    dictionary: dict[int, int] = {}

    for index, value in enumerate(nums):
        complement = target - value

        if complement in dictionary:
            return [dictionary[complement], index]

        dictionary[value] = index

    raise ValueError("No solution exists")
