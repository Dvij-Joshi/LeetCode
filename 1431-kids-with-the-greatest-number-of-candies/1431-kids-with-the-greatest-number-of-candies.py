class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        NumSum=0
        maxSum=max(candies)
        result=[]
        for i in range(len(candies)):
            NumSum=candies[i]+extraCandies
            if NumSum>=maxSum:
                result.append(True)
            else:
                result.append(False)
        return result