class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # count=0
        # seen=set()
        # candyEat=len(candyType)//2
        # for i in range(len(candyType)):
        #     if candyType[i] not in seen:
        #         count+=1
        #         seen.add(candyType[i])
        # if candyEat<=count:
        #     return candyEat
        # else:
        #     return count
        return min(len(set(candyType)),len(candyType)//2)