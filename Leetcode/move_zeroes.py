# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=programming-skills

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(len(nums)):
            if not nums[i] == 0:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1


if __name__ == '__main__':
    arr = [0, 1, 0, 3, 12]
    Solution().moveZeroes(arr)
    print(arr)
