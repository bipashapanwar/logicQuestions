class Solution(object):
    def containsDuplicate(self, nums):
        seen=set() #set because lookup is faster
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        