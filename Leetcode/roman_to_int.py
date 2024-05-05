# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=programming-skills

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        i = 0
        res = 0
        while i < len(s) - 1:
            if values[s[i + 1]] > values[s[i]]:
                res += values[s[i + 1]] - values[s[i]]
                i += 2
            else:
                res += values[s[i]]
                i += 1

        if i < len(s):
            res += values[s[i]]
        return res


if __name__ == '__main__':
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))
