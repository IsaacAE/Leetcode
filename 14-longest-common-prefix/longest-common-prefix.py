class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        prefix = ""
        for i in range(len(word)):
            guess = word[:i+1]
            for s in strs:
                if guess != s[:i+1] or i >= len(s):
                    return prefix
            prefix = guess
        
        return prefix

        