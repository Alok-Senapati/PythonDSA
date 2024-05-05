# https://leetcode.com/problems/find-the-difference/?envType=study-plan-v2&envId=programming-skills

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = Counter(s)
        for c in t:
            if not letters.get(c) or letters.get(c) == 0:
                return c
            else:
                letters[c] -= 1


if __name__ == '__main__':
    print(Solution().findTheDifference("abcd", "abcde"))
    print(Solution().findTheDifference("a", "aa"))
