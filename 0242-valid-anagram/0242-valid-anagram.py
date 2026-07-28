class Solution(object):
    def isAnagram(self, s, t):
        count={} #empty dictionary to store frequencies
        #if len is unequal, can't be anagram
        if len(s)!=len(t):
            return False
        for i in s:
            count[i]=count.get(i,0)+1 #set frequencies
        for i in t:
            count[i]=count.get(i,0)-1 #remove frequencies
            if count.get(i)<0: 
                return False
        return True
        