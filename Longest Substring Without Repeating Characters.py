class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        right=0
        max_length=0
        setf=set()

        while right<len(s):
            if s[right] not in setf:
                setf.add(s[right])
                right+=1

                max_length=max(max_length,right-left)
            
            else:
                setf.remove(s[left])
                left+=1

        return max_length


#a b c a b c b b 


#set
