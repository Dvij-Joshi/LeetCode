class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen1=set(nums1)
        seen2=set(nums2)
        result=[]
        temp=[]
        for num in seen1:
            if num not in seen2:
                temp.append(num)
        result.append(temp)
        temp=[]
        for num in seen2:
            if num not in seen1:
                temp.append(num)
        result.append(temp)
        return result
        