"""

18. 4Sum
Solved
Medium

Topics
Companies
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        n = len(nums)

        nums.sort()
        for first_iterator in range(n):
            for second_iterator in range(first_iterator+1, n):
                left_pointer = second_iterator+1; right_pointer = n-1
                while left_pointer<right_pointer:
                    sums = nums[first_iterator]+nums[second_iterator]+nums[left_pointer]+nums[right_pointer]
                    if sums < target:
                        left_pointer += 1
                    elif sums > target:
                        right_pointer -= 1
                    else:
                        toappend = [nums[first_iterator],nums[second_iterator],nums[left_pointer],nums[right_pointer]]
                        if toappend not in res:
                            res.append(toappend)
                        left_pointer +=1
                        right_pointer -=1
        return res