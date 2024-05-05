# https://leetcode.com/problems/to-lower-case/description/?envType=study-plan-v2&envId=programming-skills


class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(map(lambda x:
                           chr(ord("a") + (ord(x) - ord("A"))) if ord(x) >= ord("A") and ord(x) <= ord("Z") else x
                           , list(s)))


if __name__ == '__main__':
    print(Solution().toLowerCase("Hello"))
    print(Solution().toLowerCase("here"))
    print(Solution().toLowerCase("LOVELY"))
