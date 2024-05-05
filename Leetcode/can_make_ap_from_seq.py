# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/?envType=study-plan-v2&envId=programming-skills

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_value = min(arr)
        max_value = max(arr)

        if (max_value - min_value) % (len(arr) - 1) != 0:
            return False

        diff = (max_value - min_value) / (len(arr) - 1)
        i = 0

        while i < len(arr):
            if arr[i] == min_value + (diff * i):
                i += 1
            elif (arr[i] - min_value) % diff != 0:
                return False
            else:
                j = int((arr[i] - min_value) / diff)
                if arr[i] == arr[j]:
                    return False
                arr[i], arr[j] = arr[j], arr[i]

        return True


if __name__ == '__main__':
    print(Solution().canMakeArithmeticProgression([3, 5, 1]))
    print(Solution().canMakeArithmeticProgression([1, 2, 4]))
