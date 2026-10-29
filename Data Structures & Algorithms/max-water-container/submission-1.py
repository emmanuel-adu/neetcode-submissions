from itertools import combinations
from math import prod

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two pointer approach o(n^2)
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            area = (right - left) * min(left_height, right_height)
            max_area = max(area, max_area)

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_area

