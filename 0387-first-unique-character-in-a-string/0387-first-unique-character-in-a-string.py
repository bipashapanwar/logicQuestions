class Solution(object):
    def firstUniqChar(self, s):
        count={}
        for i in s:
            count[i]=count.get(i,0)+1
        for i in range(len(s)):
            if count.get(s[i])==1:
                return i
        return -1

        