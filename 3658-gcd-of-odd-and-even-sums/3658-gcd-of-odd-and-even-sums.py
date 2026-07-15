class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return math.gcd(n*n, n*n + n)
