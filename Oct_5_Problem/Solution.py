# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         minRepVal = len(nums)/3
#         myDict = {}
#         returned = []
#         for num in nums:
#             if num not in myDict:
#                 myDict[num] = 1
#             else:
#                 myDict[num] += 1
#             if myDict[num] > minRepVal and num not in returned:
#                 returned.insert(-1, num)
#         return returned

import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minRepVal = len(nums)//3
        x = list(set(nums))
        returned = []
        for num in x:
            if nums.count(num) > minRepVal:
                returned.append(num)
        return returned            
        

# class Solution:
#     def majorityElement(self, nums):
#         return [num for num, count in Counter(nums).items() if count > len(nums) // 3]