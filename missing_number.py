from typing import List

"""Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i not in nums:
                print(i)
                return i

s = Solution()
list1 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
list2 = [0, 1, 3]

s.missingNumber(nums=list1)
