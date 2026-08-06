class Solution(object):
    def reverseString(self, s):
        leftIndex,rightIndex=0,len(s)-1
        temp=''
        while leftIndex<rightIndex:
            temp=s[leftIndex]
            s[leftIndex]=s[rightIndex]
            s[rightIndex]=temp
            leftIndex+=1
            rightIndex-=1

            



        