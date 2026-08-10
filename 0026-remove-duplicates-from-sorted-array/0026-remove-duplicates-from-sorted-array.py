class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        left = 1
        right = 1
        while right < n:
            if nums[right]!=nums[left-1]:
                nums[left]=nums[right]
                left+=1
            right+=1
        return left
