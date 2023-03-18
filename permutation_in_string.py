class Solution(object):
    def checkInclusion(self, s1, s2):
        s1map={}
        s2map={}

        for char in s1:
            s1map[char]= 1 + s1map.get(char,0)
        
        left, right =0,0

        while right < len(s2):
            s2map[s2[right]] = 1 + s2map.get(s2[right],0)

            if right-left+1>len(s1):
                s2map[s2[left]]-=1
                if s2map[s2[left]]==0:
                    del s2map[s2[left]]
                left+=1

            if s1map == s2map:
                return True
            
            right+=1

        return False


        

