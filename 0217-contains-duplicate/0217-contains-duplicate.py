class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset=set()
        i=0
        while i<len(nums):
            if nums[i] in numset:
                return True
            else:
                numset.add(nums[i])
            i+=1
        return False
