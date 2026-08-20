class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result=[]
        # seen=set(nums1)
        # for num in nums2:
        #     if num in seen:
        #         if num not in result:
        #             result.append(num)
        # return result
        return list(set(nums1) & set(nums2))