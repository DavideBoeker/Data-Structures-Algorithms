"""

164. Maximum Gap
Medium

Topics
Companies
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109

"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_diff = 0
        n = len(nums)
        
        if n < 2:
            return max_diff

        nums.sort()

        for i in range(n-1):
            left, right = nums[i], nums[i+1]
            current_diff = nums[i+1] - nums[i]

            if current_diff > max_diff:
                max_diff = current_diff

        return max_diff