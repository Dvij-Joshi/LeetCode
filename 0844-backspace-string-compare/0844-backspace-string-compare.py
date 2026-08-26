class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack=[]
        t_stack=[]
        for ch in s:
            if ch!='#':
                s_stack.append(ch)
            elif len(s_stack)!=0:
                s_stack.pop()
        for ch in t:
            if ch!='#':
                t_stack.append(ch)
            elif len(t_stack)!=0:
                t_stack.pop()
        return s_stack==t_stack
        # pointer_s=len(s)-1   
        # pointer_t=len(t)-1
        # while pointer_s>=0 and pointer_t>=0 and s[pointer_s]==t[pointer_t]:
        #     if s[pointer_s]=='#':
        #         pointer_s-=2
        #     if t[pointer_t]=='#':
        #         pointer_t-=2
        #     pointer_t-=1
        #     pointer_s-=1
        # if pointer_s!=0:
        #     return False
        # return True
                