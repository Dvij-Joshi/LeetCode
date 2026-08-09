class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # seen={}
        # lenS=len(s)
        # lenT=len(t)
        # if lenS!=lenT:
        #     return False
        # for i in range(lenS):
        #     seen[s[i]]=seen.get(s[i],0)+1
        # for i in range(lenT):
        #     if t[i] not in seen or seen[t[i]]==0:
        #         return False
        #     seen[t[i]]-=1
        # return True
        return Counter(s)==Counter(t)