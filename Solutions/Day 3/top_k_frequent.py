class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1={}
        for n in nums:
            if n in d1:
                d1[n]+=1
            else:
                d1[n]=1
        sorted_d1 = sorted(d1.items(),key=lambda x: -x[1])
        ans = []
        for k1,v in sorted_d1:
            ans.append(k1)
        return ans[:k]                