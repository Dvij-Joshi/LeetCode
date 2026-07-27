class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast=slow=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                # return nums[slow]
                break
        n1=0
        n2=slow
        while n1!=n2:
            n1=nums[n1]
            n2=nums[n2]
        return n1