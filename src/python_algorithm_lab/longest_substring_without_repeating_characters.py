"""https://leetcode.com/problems/longest-substring-without-repeating-characters/"""


def length_of_longest_substring_brute_force(s: str) -> int:
    """Time: O(n²), Space: O(n)"""
    max_length = 0

    for start_index, start_character in enumerate(s):
        seen = set(start_character)
        for end_index in range(start_index + 1, len(s)):
            end_character = s[end_index]
            if end_character in seen:
                break
            seen.add(end_character)
        max_length = max(max_length, len(seen))

    return max_length


def length_of_longest_substring_sliding_window(s: str) -> int:
    """Time: O(n), Space: O(n)"""
    max_length = 0
    left = 0
    seen: set[str] = set()

    for right in range(0, len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
