# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=programming-skills


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1].strip())


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
    print(Solution().lengthOfLastWord("luffy is still joyboy"))
