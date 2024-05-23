"""

75. Sort Colors
Solved
Medium

Topics
Companies

Hint
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

         # Initialize pointers
        left = 0
        right = len(nums) - 1
        current = 0

        # Traverse the array
        while current <= right:
            if nums[current] == 0:
                # Swap 0s to the left
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
                current += 1
            elif nums[current] == 2:
                # Swap 2s to the right
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                # Increment current pointer for 1s
                current += 1
            
    
    def sortColors_standard(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

         # Use built in TIMSORT method
        nums.sort()