"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Return  most common element is the element that appears more than n // 2 times
    and the least common element"""
    most_common_elem, least_common_elem = (
        Counter(inp).most_common()[0],
        Counter(inp).most_common()[-1],
    )

    if most_common_elem[1] <= len(inp) // 2:
        raise ValueError("Most common element appears less than n // 2 times ")

    return most_common_elem[0], least_common_elem[0]
