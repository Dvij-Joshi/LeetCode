class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # val=Counter(nums)
        # key=min(val.values())
        # for i,value in val.items():
        #     if value==key:
        #         return i
        result=0
        for num in nums:
            result^=num
        return result