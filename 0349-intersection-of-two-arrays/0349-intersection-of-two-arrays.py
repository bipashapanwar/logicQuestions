class Solution(object):
    def intersection(self, nums1, nums2):
        intersection=set()
        nums2=set(nums2)
        for num in nums1:
            if num in nums2:
                intersection.add(num)
        return list(intersection)

        