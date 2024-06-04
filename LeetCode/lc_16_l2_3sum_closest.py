"""

16. 3Sum Closest
Medium

Topics
Companies
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        closest_sum = None
        n = len(nums)

        for i in range(n - 2):

            left, right = i + 1, n - 1
            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]
                if closest_sum == None:
                    closest_sum = current_sum
                elif abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # Move pointers based on comparison of current_sum and target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest_sum