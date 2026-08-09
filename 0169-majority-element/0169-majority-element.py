class Solution(object):
    #solve using Boyer-Moore's algo later
    def majorityElement(self, nums):
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]>(len(nums)/2):
               return i
        