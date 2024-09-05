from typing import List

nums = [2, 7, 11, 15]
target = 9


def two_sum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i


if __name__ == "__main__":
    print(two_sum(nums, target))
