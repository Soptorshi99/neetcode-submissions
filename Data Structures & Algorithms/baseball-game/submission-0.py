class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for el in operations:
            if el=="+":
                a=stack[-1]
                b=stack[-2]
                stack.append(a+b)
            elif el=="C":
                stack.pop()
            elif el=="D":
                a=stack[-1]
                stack.append(2*a)
            else:
                stack.append(int(el))
        return sum(stack)