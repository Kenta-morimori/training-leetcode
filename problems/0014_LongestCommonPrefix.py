"""
共通する最大の接頭辞を求める
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix_chars = []
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix_chars.append(chars[0])
            else:
                break
        return "".join(prefix_chars)


"""
memo:

- zip(*strs)
```
strs = ["flower", "flow", "flight"]
list(zip(*strs))
-> [('f','f','f'), ('l','l','l'), ('o','o','i'), ('w','w','g')]
```
その後，全て同じ文字化を確認している．

- "".join(prefix_chars)
文字列をまとめる

"""
