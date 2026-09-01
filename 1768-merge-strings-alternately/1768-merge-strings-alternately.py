class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wrd1=len(word1)
        wrd2=len(word2)
        left=right=0
        result=[]
        while left<wrd1 or right<wrd2:
            if left==wrd1:
                result.append(word2[right])
                right+=1
            elif right==wrd2:
                result.append(word1[left])
                left+=1
            else:
                result.append(word1[left])
                result.append(word2[right])
                left+=1
                right+=1
        return ''.join(result)