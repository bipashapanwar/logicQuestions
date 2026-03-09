class Solution(object):
    def twoSum(self, nums, target):
        seen={} #hashmap or dictionary for fast lookup
        for i,num in enumerate(nums):
            complement=target-num

            if complement in seen:
                return(seen[complement],i)
            
            seen[num]=i

        