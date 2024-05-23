
"""

349. Intersection of Two Arrays
Easy

Topics
Companies
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert the lists to sets to utilize set intersection operation
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection using set intersection operation
        intersection_set = set1.intersection(set2)
        
        # Convert the resulting set back to a list
        intersection_list = list(intersection_set)
        
        return intersection_list
    

    def intersection_ii(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Create a dictionary to store the elements of nums1
        num_counts = {}
        for num in nums1:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        # Iterate through nums2 and check for intersection
        intersection = []
        for num in nums2:
            if num in num_counts and num not in intersection:
                intersection.append(num)
        
        return intersection