class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for el in s:
            if el in {"(","{","["}:
                stack.append(el)
            else:
                if el==")":
                    if stack and stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                elif el=="}":
                    if stack and stack[-1]=="{":
                        stack.pop()
                    else:
                        return False
                elif el=="]":
                    if stack and stack[-1]=="[":
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        return False