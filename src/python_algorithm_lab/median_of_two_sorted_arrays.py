"""https://leetcode.com/problems/median-of-two-sorted-arrays/"""


def find_median_sorted_arrays_easy(nums1: list[int], nums2: list[int]) -> float:
    """Time: O(nlogn), Space: O(n)"""
    combined = sorted(nums1 + nums2)

    length = len(combined)
    index = length // 2
    if length % 2 == 0:
        return (combined[index - 1] + combined[index]) / 2
    else:
        return combined[index]


def find_median_sorted_arrays_merge_sort(nums1: list[int], nums2: list[int]) -> float:
    """Time: O(n), Space: O(1)"""
    count = pointer1 = pointer2 = 0
    current_value = previous_value = None

    total_length = len(nums1) + len(nums2)
    stop_length = total_length // 2

    while count <= stop_length:
        previous_value = current_value
        if pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] <= nums2[pointer2]:
                current_value = nums1[pointer1]
                pointer1 += 1
            else:
                current_value = nums2[pointer2]
                pointer2 += 1
        elif pointer1 >= len(nums1):
            current_value = nums2[pointer2]
            pointer2 += 1
        else:
            current_value = nums1[pointer1]
            pointer1 += 1
        count += 1

    if total_length % 2 == 0:
        return (current_value + previous_value) / 2
    else:
        return current_value
