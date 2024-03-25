class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        countT={}
        reslen=float("infinity")
        
        for c in t:
            countT[c] = countT.get(c,0)+1
        l,r=0,0
        res=[-1,-1]
        have,need=0,len(countT)
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            if s[r] in countT and countT[s[r]]==window[s[r]]:
                have+=1
            while have==need:
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                if (r-l+1)<reslen:
                    reslen = (r-l+1)
                    res=[l,r]
                l+=1    
        l,r=res
        return s[l:r+1]                    
            