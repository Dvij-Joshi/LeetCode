class Solution:
    def isHappy(self, num: int) -> bool:
        def helper(n: int):
            sum = 0 
            while n>0:
                dig = n%10
                sum+=(dig*dig)
                n=n//10
            return sum
        slow=num
        fast=num
        while fast != 1:
            slow=helper(slow)
            fast=helper(helper(fast))
            if fast==1:
                return True
            if fast==slow:
                return False
        return True