class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre={}
        for num in nums:
            if num in fre:
                fre[num]+=1
            else:
                fre[num]=1
        result=sorted(fre,key=fre.get,reverse=True)[:k]
        return result
