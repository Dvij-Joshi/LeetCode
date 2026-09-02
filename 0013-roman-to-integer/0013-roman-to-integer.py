class Solution:
    def romanToInt(self, s: str) -> int:
        symbol={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        stack=[]
        for i in range(len(s)):
            if stack and stack[-1]<symbol.get(s[i]):
                result=symbol.get(s[i])-stack[-1]
                stack.pop()
                stack.append(result)
            else:
                stack.append(symbol.get(s[i]))
        return sum(stack)
