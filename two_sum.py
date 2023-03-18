class Solution(object):
    def twoSum(self, nums, target):
        twosum={}
        for i in range(len(nums)):
            remain_num=target-nums[i]
            if remain_num in twosum:
                return [twosum[remain_num],i]
            twosum[nums[i]]=i
