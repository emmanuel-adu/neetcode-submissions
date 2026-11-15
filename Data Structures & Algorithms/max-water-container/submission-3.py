class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left

            # move pointer at lower height
            if heights[left] < heights[right]:
                area = width * heights[left]
                left += 1
            else:
                area = width * heights[right]
                right -= 1

            max_area = max(area, max_area)
        return max_area

        