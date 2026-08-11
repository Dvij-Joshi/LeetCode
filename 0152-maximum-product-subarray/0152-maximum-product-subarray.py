class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_result=max_result=result=nums[0]
        for i in range(1,len(nums)):
            candidates=(nums[i],min_result*nums[i],max_result*nums[i])
            min_result=min(candidates)
            max_result=max(candidates)
            result=max(result,max_result)
        return result