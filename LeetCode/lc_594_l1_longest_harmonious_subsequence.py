"""

594. Longest Harmonious Subsequence
Easy

Topics
Companies
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0
 

Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109

"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(set(nums)) <= 1:
            return 0

        nums.sort()
        max_count = 0
        i = 0

        while i < len(nums):
            j = i
            left = nums[i]
            right = left
            while j < len(nums) and nums[j] - left <= 1:
                right = nums[j]
                j += 1
            if right - left == 1:
                temp_count = j - i
                if temp_count > max_count:
                    max_count = temp_count
            i += 1

        return max_count



    def findLHS_shorter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        max_length = 0
        for num in count:
            if num + 1 in count:
                max_length = max(max_length, count[num] + count[num + 1])
        
        return max_length