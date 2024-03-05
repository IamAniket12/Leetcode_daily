class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        ans = 0
        stock=[]
        while l<=r and r<len(s):
            if s[r] in stock:
                while s[r] in stock:
                    stock.remove(s[l])
                    l+=1
            stock.append(s[r])           
            ans = max(ans,(r-l+1))
            r+=1
        
        return ans      
                      
        
        