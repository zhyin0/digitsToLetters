from typing import List
import re

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "0": [""],
            "1": [""],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        li = []
        for i in digits:
            li.append(dic[i])
        n = len(li)
        if n == 1:
            return li[0]
        elif n == 0:
            return li
        li_grow = [""]
        for i in range(n):
            li_now = []
            for j in li[i]:
                for x in li_grow:
                    li_now.append(x+j)
            li_grow = li_now.copy()
        return li_grow


if __name__ == '__main__':
    n = input("Please enter an integer from 0 to 99:")
    while (re.match("[0-9]{1,2}$", n) == None):
        n = input("Illegal input! Only integers from 0 to 99 are supported. Please re-enter：")
    print(Solution.letterCombinations(Solution, n))
