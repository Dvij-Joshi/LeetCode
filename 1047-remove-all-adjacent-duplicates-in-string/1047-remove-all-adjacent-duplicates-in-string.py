class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for ch in s:
            if stack and stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
        # length=0
        # right=0
        # while right<len(s):
        #     if right>=2 and length>=2 and stack[-1]==stack[-2]:
        #         stack.pop()
        #         stack.pop()
        #         length-=2
        #     else:
        #         stack.append(s[right])
        #         length+=1
        #         right+=1
        # if length>=2 and stack[-1]==stack[-2]:
        #     stack.pop()
        #     stack.pop()
        # return ''.join(stack)