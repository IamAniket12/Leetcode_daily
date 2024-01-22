class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d1={}
        for n in nums:
            if n in d1:
                return True
            else:
                d1[n]=1
        return False           