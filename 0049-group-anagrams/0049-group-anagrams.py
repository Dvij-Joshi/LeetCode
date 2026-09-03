class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dic={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in sorted_dic:
                sorted_dic[key]=[]
            sorted_dic[key].append(word)
        return list(sorted_dic.values())