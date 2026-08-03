class Solution(object):
    def sumOfUnique(self, nums):
        count={}
        sum=0
        for i in nums:
            count[i]=count.get(i,0)+1
        for i in count:
            if count[i]==1:
                sum+=i
        return sum
        
        