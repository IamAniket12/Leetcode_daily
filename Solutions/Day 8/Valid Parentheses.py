class Solution:
    def isValid(self, s: str) -> bool:
        d1 = {')':'(','}':'{',']':'['}
        stack=[]
        for c in s:
            if c=='(' or c=='{' or c=='[':
                stack.append(c)
            else:
                if stack:
                    temp=stack.pop()
                    if temp!=d1[c]:
                        return False
                else:
                    return False        
        return len(stack)==0      