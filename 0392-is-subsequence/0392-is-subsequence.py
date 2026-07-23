class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerS=0
        pointerT=0
        if len(s)==0: 
            return True
        if len(t)==0:
            return False
        while pointerT<len(t):
            if s[pointerS]==t[pointerT]:
                pointerS+=1
                pointerT+=1
            else:
                pointerT+=1
            if(pointerS==len(s)):
                return True
        return False