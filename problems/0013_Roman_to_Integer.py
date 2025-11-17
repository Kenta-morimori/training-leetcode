"""
ローマ字を認識する

https://leetcode.com/problems/roman-to-integer?envType=problem-list-v2&envId=v3q3zk5s
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        counts = 0
        count_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for a, b in zip(s, s[1:]):
            if count_dict[a] < count_dict[b]:
                counts -= count_dict[a]
            else:
                counts += count_dict[a]

        return counts + count_dict[s[-1]] 


"""
memo:

- `for a, b in zip(s, s[1:]):`で隣り合う2つをマッピングできる
- 大小関係に応じて加減算

"""
