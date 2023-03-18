class Solution(object):
    def topKFrequent(self, nums, k):
        count={}
        frequency=[[] for i in range(len(nums)+1)]

        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            frequency[c].append(n)

        res=[]
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                res.append(n)
                if len(res)==k:
                    return res



        '''1,1,1,2,4,4

        count:
        (key)   (value)
        n       c
        1       3
        2       1
        4       2


        n   c in count.items():
        freq:
        (index) (value)
        3       1
        1       2
        2       4'''



