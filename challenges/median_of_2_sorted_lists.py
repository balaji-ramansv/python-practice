from ast import List
from statistics import median


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        combined = nums1 + nums2
        combined.sort()
        return median(combined)

print(Solution().findMedianSortedArrays([1,3], [2]))