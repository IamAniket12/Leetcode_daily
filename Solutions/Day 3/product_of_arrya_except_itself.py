class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftm = [1]*len(nums)
        rightm = [1]*len(nums)
        leftm[0]=nums[0]
        rightm[-1]=nums[-1]
        ans = [0]*len(nums)
        mul = 1
        for i in range(1,len(nums)):
            leftm[i] = leftm[i-1]*nums[i]
        for r in range(len(nums)-2,-1,-1):
            rightm[r] = rightm[r+1]*nums[r] 
        ans[0]=rightm[1]
        ans[-1] = leftm[-2]   
        for i in range(1,len(nums)-1):
            ans[i] = leftm[i-1]*rightm[i+1]    
        return ans