# https://leetcode.com/problems/baseball-game/description/?envType=study-plan-v2&envId=programming-skills

from typing import List
from queue import LifoQueue

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = LifoQueue(maxsize=len(operations))
        for operator in operations:
            if operator.isnumeric() or (operator.startswith("-") and operator[1:].isnumeric()):
                stack.put(int(operator))
            elif operator == "C":
                stack.get()
            elif operator == "D":
                top = stack.get()
                d = top * 2
                stack.put(top)
                stack.put(d)
            elif operator == "+":
                first = stack.get()
                second = stack.get()
                res = first + second
                stack.put(second)
                stack.put(first)
                stack.put(res)
            else:
                raise Exception("Invalid Operator")
        total_sum = 0
        while not stack.empty():
            total_sum += int(stack.get())
        return total_sum


if __name__ == '__main__':
    print(Solution().calPoints(["5","2","C","D","+"]))
    print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))
    print(Solution().calPoints(["1","C"]))
