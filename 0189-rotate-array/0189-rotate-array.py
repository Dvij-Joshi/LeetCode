class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate_right(lst, k):
            k = k % len(lst)
            return lst[-k:] + lst[:-k]
        nums[:]=rotate_right(nums,k)
        # left=0
        # right=len(nums)-1
        # temp=0
        # while left<right:
        #     temp=nums[left]
        #     nums[left]=nums[right]
        #     nums[right]=temp
        #     left+=1
        #     right-=1
            