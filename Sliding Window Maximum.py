class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n=len(nums)
        if n==0:
            return []
        if k==1:
            return nums
        q=deque() #index
        res=[]
        for i in range(n):


            #remove elements smaller than current element
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)

            #remove element outside the window

            while q and q[0]<i-k+1:
                q.popleft()

            #storing the result
            if i>=k-1:
                res.append(nums[q[0]])
            


        return res

        








