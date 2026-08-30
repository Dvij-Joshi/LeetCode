class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        s_len=len(s)
        if s_len==1:
            return 1
        right=s_len-1
        print(right)
        count=0
        while right!=-1:
            if s[right]!=' ':
                count+=1
                right-=1
            else:
                break
        return count