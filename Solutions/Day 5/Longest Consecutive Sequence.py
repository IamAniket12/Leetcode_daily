class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        set_nums=set(nums)
        for n in nums:
            #it can be starting of the nums
            if (n-1) not in set_nums:
                length=0
                while n+length in set_nums:
                    length+=1
                longest = max(length,longest)
        return longest            
        