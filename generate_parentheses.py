class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def backtrack(s='',openB=0,closeB=0):
            if len(s)==2*n:
                res.append(s)
                return

            if openB<n:
                backtrack(s+'(',openB+1,closeB)
            if closeB<openB:
                backtrack(s+')',openB,closeB+1)
        backtrack()
        return res
