class Solution(object):
    def runningSum(self, nums):
        aans=[]
        total=0
        for num in nums:
            total+=num
            aans.append(total)
        return aans

        