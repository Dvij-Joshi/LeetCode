class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        i=0
        l=len(nums)
        count=0
        while i < l:
            while nums[i]!=0:
                nums[i]=nums[i] // 10
                count+=1
            if(count%2==0):
                even+=1
                count=0
            else:
                count=0
            i+=1
        return even
        