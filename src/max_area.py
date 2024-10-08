from typing import List


def maxArea(height: List[int]) -> int:
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


test_cases = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(test_cases))
