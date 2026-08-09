class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        hm=Counter(nums)
        rev=sorted(hm.items(),key=lambda item: item[1],reverse=True)
        ans=[]
        i=0
        while k!=0:
            a=rev[i][0]
            ans.append(a)
            i=i+1
            k=k-1
        return ans