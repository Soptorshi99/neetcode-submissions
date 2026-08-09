class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            if target-nums[i] in hm:
                f=hm[target-nums[i]]
                return [f,i]
            hm[nums[i]]=i
