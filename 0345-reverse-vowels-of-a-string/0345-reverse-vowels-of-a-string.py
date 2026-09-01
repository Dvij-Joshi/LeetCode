class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u']
        left=0
        right=len(s)-1
        s=list(s)
        while left<right:
            if left<len(s) and s[left].lower() in vowels:
                if s[right].lower() in vowels:
                    s[left],s[right]=s[right],s[left]
                    left+=1
                    right-=1
                else:
                    right-=1
            else:
                left+=1
        return ''.join(s)