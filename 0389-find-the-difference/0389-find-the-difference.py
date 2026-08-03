class Solution(object):
    def findTheDifference(self, s, t):
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        for ch in t:
            count[ch]=count.get(ch,0)-1
            if count[ch]==-1:
               return ch
        