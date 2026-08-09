class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p=1
        n=len(nums)
        prefix_product=[1]*n
        sufffix_product=[1]*n

        for i in range(1,n):
            prefix_product[i]=prefix_product[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            sufffix_product[i]=sufffix_product[i+1]*nums[i+1]
        ans=[]
        for i in range(n):
            a=prefix_product[i]*sufffix_product[i]
            ans.append(a)
        return ans