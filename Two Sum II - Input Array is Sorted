class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        while left<right:
            current_val=numbers[left] + numbers[right]
            if current_val==target:
                return [left+1, right+1]
            elif current_val<target:
                left+=1
            else:
                right-=1
            
        return [-1,-1]

