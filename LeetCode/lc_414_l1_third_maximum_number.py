"""

414. Third Maximum Number
Solved
Easy

Topics
Companies
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?

"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = set(nums)
        nums = list(nums)

        nums.sort(reverse=True)

        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]
        


    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        first_max = second_max = third_max = float('-inf')
        
        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max and num != first_max:
                third_max = second_max
                second_max = num
            elif num > third_max and num != second_max and num != first_max:
                third_max = num
                
        if third_max != float('-inf'):
            return third_max
        else:
            return first_max