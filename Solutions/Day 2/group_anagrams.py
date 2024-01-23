class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = defaultdict(list)

        for s in strs:
            l1 = [0]*26
            for c in s:
                l1[ord(c)-97]+=1
            d1[tuple(l1)].append(s)
        return d1.values()        