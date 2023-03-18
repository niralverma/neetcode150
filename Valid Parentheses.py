class Solution(object):
    def isValid(self, s):
        stack=[]
        for bracket in s:
            if bracket in ["(","{","["]:
                stack.append(bracket)
            elif bracket == ")":
                if not stack or stack[-1]!="(":
                    return False
                stack.pop()
            elif bracket == "}":
                if not stack or stack[-1]!="{":
                    return False
                stack.pop()
            elif bracket == "]":
                if not stack or stack[-1]!="[":
                    return False
                stack.pop()
        return not stack

            


