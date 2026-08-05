class Solution(object):
    def repeatedCharacter(self, s):
        count={}
        for i in s:
            count[i]=count.get(i,0)+1
            if count[i]==2:
                return i

        