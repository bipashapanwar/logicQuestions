class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        indexMap={}
        for i in range(len(nums)):
            if nums[i] in indexMap:
                if abs(i-indexMap[nums[i]])<=k:
                    return True
            indexMap[nums[i]]=i
        return False
            

        