from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        return [i for i in range(1, n+1) if i not in nums_set]
