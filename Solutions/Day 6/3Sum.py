class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans=[]
        target=0
        i=0
        while i < len(nums): 
            first = nums[i]
            left = i+1
            right=len(nums)-1
            while left<right:
                if first+nums[left]+nums[right]==target:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1    
                elif first+nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return ans                                        


        