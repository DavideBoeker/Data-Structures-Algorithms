"""

215. Kth Largest Element in an Array
Solved
Medium

Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

"""
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Sort the list in descending order
        nums.sort(reverse=True)

        # Return the kth element (0-based indexing)
        return nums[k - 1]
    

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Initialize an empty list
        k_numbers_min_heap = []

        # Add first k elements to the list
        for i in range(k):
            k_numbers_min_heap.append(nums[i])

        # Convert the list into a min-heap
        heapq.heapify(k_numbers_min_heap)

        # Loop through the remaining elements in the 'nums' array
        for i in range(k, len(nums)):
            # Compare the current element with the minimum
            # element (root) of the min-heap
            if nums[i] > k_numbers_min_heap[0]:
                # Remove the smallest element
                heapq.heappop(k_numbers_min_heap)
                # Add the current element
                heapq.heappush(k_numbers_min_heap, nums[i])

        # The root of the heap has the Kth largest element
        return k_numbers_min_heap[0]