# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list = nums1+nums2
        list.sort()
        length = len(list)
        midPoint = int(length / 2)
        value = 0

        if length % 2 == 0:
            value = (list[midPoint-1] + list[midPoint]) / 2
        else:
            value = list[midPoint]



        return value



if __name__ == '__main__':
    '''
    nums1 = [1, 2]
    nums2 = [3, 4]
    '''
    nums1 = [1, 3]
    nums2 = [2]


    print(Solution.findMedianSortedArrays(Solution,nums1,nums2))

