class Solution:
    def reverseWords(self, s: str) -> str:
        j = i = len(s) - 1
        substring = ''
        while s[j] == ' ':
            j -= 1
            i -= 1
        while j >=0: 
            if j>=0 and s[j] != ' ':
                # i -= 1
                j -= 1
            else:
                temp = j
                j += 1

                while j <= i:
                    substring += s[j]
                    j += 1
                substring+=' ' 
                i = temp
                while i >= 0 and s[i] == ' ':
                    i -= 1
                j=i
        j+=1
        while j <= i:
            substring += s[j]
            j += 1
        return substring.strip()