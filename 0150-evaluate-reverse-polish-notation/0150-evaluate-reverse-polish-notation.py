class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit():
                stack.append(int(tokens[i]))
            elif tokens[i]=='+':
                temp1=stack.pop()
                temp2=stack.pop()
                result=temp1+temp2
                stack.append(result)
            elif tokens[i]=='-':
                temp1=stack.pop()
                temp2=stack.pop()
                result=temp2-temp1
                stack.append(result)
            elif tokens[i]=='/':
                temp1=stack.pop()
                temp2=stack.pop()
                result=int(temp2/temp1)
                stack.append(result)
            elif tokens[i]=='*':
                temp1=stack.pop()
                temp2=stack.pop()
                print(temp1,temp2)
                result=temp1*temp2
                stack.append(result)
        return stack[-1]

                

