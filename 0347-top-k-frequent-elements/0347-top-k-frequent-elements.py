class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre={}
        # for num in nums:
        #     if num in fre:
        #         fre[num]+=1
        #     else:
        #         fre[num]=1
        # result=sorted(fre,key=fre.get,reverse=True)[:k]
        # return result
        my_count = Counter(nums)
        # print(my_count)
        result=[item for item,count in my_count.most_common(k) ]
        return result
        # return count.most_common(k)
