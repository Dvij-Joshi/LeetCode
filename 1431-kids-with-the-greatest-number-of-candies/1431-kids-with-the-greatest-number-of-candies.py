class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        NumSum=0
        maxSum=max(candies)
        result=[]
        for i in range(len(candies)):
            NumSum=candies[i]+extraCandies
            print("Candies :",candies[i])
            print("Extra Candies :",extraCandies)
            # maxSum=max(maxSum,NumSum)
            print("NumSum :",NumSum)
            print("maxSum :",maxSum)
            if NumSum>=maxSum:
                result.append(True)
            else:
                result.append(False)
        return result