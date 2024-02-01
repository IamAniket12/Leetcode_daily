class Solution:
    def isPalindrome(self, s: str) -> bool:
        text=""
        for c in s:           
            if c.isalnum():
                c = c.lower()
                text+=c
        l=0
        r=len(text)-1
        while l<r:
            if text[l]!=text[r]:return False
            l+=1
            r-=1
        return True            