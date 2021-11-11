"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k <= 0:
        return 0
    max_sum = float("-inf")
    for i in range(len(nums)):
        start_sum = 0
        local_sums = []  # array with part sums of slice
        for j in nums[i: i + k]:
            start_sum += j
            local_sums.append(start_sum)
        local_max_sum = max(local_sums)
        if local_max_sum > max_sum:
            max_sum = local_max_sum

    return max_sum
