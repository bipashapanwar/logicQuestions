class Solution(object):
    def isPowerOfThree(self, n):
        if n==1:
            return True
        if n>0 and n%3==0:
            return self.isPowerOfThree(n/3)
        return False
        