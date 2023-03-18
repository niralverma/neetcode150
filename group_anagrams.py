class Solution(object):
    def groupAnagrams(self, strs):
        hashmap={}
        for s in strs:
            sorted_s="".join(sorted(s))
            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s]=[s]

        return list(hashmap.values())



#eat
#aet =key
