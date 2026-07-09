class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for nums in nums if len(str(abs(nums))) %2==0)
        