class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left=0
        right=0
        while left < len(s) and right<len(t): # 0,1,2,3,5,6,7,end
            if s[left]==t[right] : # c=c,s[1]=o t[1]=0,s[2]=a t[2]=d
                left+=1 # left=1,2,skip
                right+=1 #right = 1,2,skip
            else:
                left+=1 #left=3,4,6,7,8
        return len(t)-right
