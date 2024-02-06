class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(openc,closec):
            if openc==closec==n:
                ans.append("".join(stack))
            if openc<n:
                stack.append("(")
                dfs(openc+1,closec)
                stack.pop()
            if closec<openc:
                stack.append(")")
                dfs(openc,closec+1)
                stack.pop()

        stack=[]
        ans=[]
        dfs(0,0)
        return ans
        