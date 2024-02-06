class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op = ['+','-','*','/']
        for t in tokens:
            print(stack)
            if t in op:
                temp1 = stack.pop()
                temp2 =stack.pop()
                if t=='+':
                    stack.append(temp1+temp2)
                elif t=='-':
                    stack.append(temp2-temp1)
                elif t=='*':
                    stack.append(temp1*temp2)
                else:
                    stack.append(int(temp2/temp1))
            else:
                stack.append(int(t))
        return stack[0]                            