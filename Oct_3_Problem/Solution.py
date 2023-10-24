# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#         return count

# from typing import List
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:

#         diktator = {}
#         ans = 0

#         for i, num in enumerate(nums):
#             if num not in diktator:
#                 diktator[num] = 0
#             else:
#                 diktator[num] += 1
#                 ans += diktator[num]

#         return ans

import List
import collections
import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([math.comb(n, 2) for n in collections.Counter(nums).values()])      