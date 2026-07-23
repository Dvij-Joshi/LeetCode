class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerS=0
        if not s:
            return True
        for i in range(len(t)):
            if t[i]==s[pointerS]:
                pointerS+=1
            if pointerS==len(s):
                return True
        return False
