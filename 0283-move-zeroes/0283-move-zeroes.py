class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=1
        n=len(nums)
        while j<n and n>1 and i<n:
            if nums[i]==0:
                if nums[j]==0:
                    j+=1
                else:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j+=1
            else:
                i+=1
                j+=1

