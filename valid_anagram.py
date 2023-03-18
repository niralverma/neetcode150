class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        
        count={}
        for c in s:
            if c in count:
                count[c]+=1
            else:
                count[c]=1
            
        for c in t:
            if c not in count:
                return False
            count[c]-=1
            if count[c]==0:
                del count[c]
            
        return len(count)==0

        
