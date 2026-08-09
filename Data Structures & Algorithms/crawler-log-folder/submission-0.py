class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
       
        for s in logs:
            if s[0]==".":
                if s[1]==".":
                    if stack :
                        stack.pop()
                elif  s[1]=="/":
                    continue
            else:
                stack.append(s)
        return len(stack)