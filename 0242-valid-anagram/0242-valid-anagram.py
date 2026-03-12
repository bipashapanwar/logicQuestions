class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
            return False
        count={} #empty dictionary to store count for each letter
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            count[t[i]]=count.get(t[i],0)-1
        for value in count.values():
            if (value!=0):
                return False
                break

        return True
