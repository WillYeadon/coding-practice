from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        n = len(intervals)
        i = 0

        # Add all intervals that come before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # If no overlap just add as normal
        merged.append(newInterval)

        # Add all intervals that come after the new interval
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged
