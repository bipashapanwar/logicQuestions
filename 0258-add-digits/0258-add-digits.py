class Solution(object):
    def addDigits(self, num):
        '''O(logn) approach-
        sum=0
        if num==0:
            return 0
        while num>0:
            sum+=num%10
            num//=10
        if sum>9:
            return self.addDigits(sum)
        return sum'''

        #O(1) approach -
        if num<=9:
            return num
        if num%9==0:
            return 9
        return num%9
        
        

        