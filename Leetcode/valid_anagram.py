# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=programming-skills
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = Counter(s)
        for c in t:
            if c not in letters.keys() or letters.get(c) == 0:
                return False
            letters[c] -= 1
        return all(map(lambda x: x == 0, letters.values()))


if __name__ == '__main__':
    print(Solution().isAnagram("anagram", "nagaram"))
    print(Solution().isAnagram("rat", "car"))