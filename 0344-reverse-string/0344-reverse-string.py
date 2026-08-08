class Solution(object):
    def reverseString(self, s):
        leftIndex,rightIndex=0,len(s)-1
        while leftIndex<rightIndex:
            s[leftIndex],s[rightIndex]=s[rightIndex],s[leftIndex]
            leftIndex+=1
            rightIndex-=1
        return s

            



        