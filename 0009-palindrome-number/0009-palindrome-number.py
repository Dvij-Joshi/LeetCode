class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_X=x
        new_x=0
        if(x<0):
            return False
        else:
            while x!=0:
                new_x=(new_x*10)+(x%10)
                x=x//10
            if(new_x==original_X):
                return True
            else:
                return False
        