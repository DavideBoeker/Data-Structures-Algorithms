"""

56. Merge Intervals
Solved
Medium

Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = [intervals[0]]
        
        for current in intervals[1:]:
            last_merged = merged_intervals[-1]
            
            # If the current interval overlaps with the last merged interval, merge them
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add the current interval to the list
                merged_intervals.append(current)
        
        return merged_intervals