from typing import List
from functools import reduce


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = reduce(lambda x, y: x * y, nums)
        return 1 if product > 0 else -1 if product < 0 else 0


if __name__ == '__main__':
    print(Solution().arraySign([-1,-2,-3,-4,3,2,1]))
    print(Solution().arraySign([1,5,0,2,-3]))
    print(Solution().arraySign([-1,1,-1,1,-1]))