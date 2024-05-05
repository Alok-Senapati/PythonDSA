# https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=programming-skills
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            r = digits[i] + carry
            digits[i] = r % 10
            carry = r // 10
        return [carry] + digits if carry != 0 else digits


if __name__ == '__main__':
    print(Solution().plusOne([1, 2, 3]))
    print(Solution().plusOne([4, 3, 2, 1]))
    print(Solution().plusOne([9]))
