class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for el in strs:
            a=''.join(sorted(el))
            if a not in hm:
                hm[a]=[]
            hm[a].append(el)
        ans=[]
        for key,val in hm.items():
            ans.append(val)
        return ans