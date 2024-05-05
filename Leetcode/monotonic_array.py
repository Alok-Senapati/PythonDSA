# https://leetcode.com/problems/monotonic-array/description/?envType=study-plan-v2&envId=programming-skills

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = True if nums[0] <= nums[-1] else False
        for i in range(1, len(nums)):
            if isIncreasing and nums[i] < nums[i - 1]:
                return False
            elif not isIncreasing and nums[i] > nums[i - 1]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isMonotonic([1,2,2,3]))
    print(Solution().isMonotonic([6,5,4,4]))
    print(Solution().isMonotonic([1,3,2]))
