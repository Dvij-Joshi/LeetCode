class Solution:
    # def reverseVowels(self, s: str) -> str:
    #     vowels=set('aeiouAEIOU')
    #     left=0
    #     right=len(s)-1
    #     s=list(s)
    #     while left<right:
    #         if  s[left].lower() in vowels:
    #             if s[right].lower() in vowels:
    #                 s[left],s[right]=s[right],s[left]
    #                 left+=1
    #                 right-=1
    #             else:
    #                 right-=1
    #         else:
    #             left+=1
    #     return ''.join(s)
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
    
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
        return ''.join(s)