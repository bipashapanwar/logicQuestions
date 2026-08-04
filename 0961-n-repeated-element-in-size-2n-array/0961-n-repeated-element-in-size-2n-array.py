class Solution(object):
    def repeatedNTimes(self, nums):
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
            if count[i]>1:
                return i
        
            
        