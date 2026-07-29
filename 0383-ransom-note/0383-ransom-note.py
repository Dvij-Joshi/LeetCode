class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        left=0
        right=0
        ransomNote=sorted(ransomNote)
        magazine=sorted(magazine)
        while right<len(magazine) and left<len(ransomNote):#1: 0<3 and 0<3, 2: 1<3 and 0<3
            if ransomNote[left]==magazine[right]: # 1: if a==b. 2: a==bT
                left+=1
                right+=1
            else:
                right+=1 #1: right = 1
        if left == len(ransomNote):
                return True
        else:
            return False