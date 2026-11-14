class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # calculate area of water
        # area = width * height
        # width = right - left
        # height = given

        # calculate area for left height and right height
        # then return max area
        max_area = float("-inf")

        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left

            # calculate area
            if heights[left] < heights[right]:
                current_area = width * heights[left]
                left += 1
            else:
                current_area = width * heights[right]
                right -= 1
            
            # max area
            max_area = max(current_area, max_area)
        
        return max_area
        