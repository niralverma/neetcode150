class Solution(object):
    def permute(self, nums):
        res=[]
        def backtrack(path):
            if len(path)==len(nums):
                res.append(path)
            for num in nums:
                if num not in path:
                    backtrack(path+[num])

        backtrack([])
        return res
