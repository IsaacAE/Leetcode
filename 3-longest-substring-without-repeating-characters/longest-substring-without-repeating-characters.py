class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        length = 0
        start = 0
        
        for i in range(len(s)):
            char = s[i]
            if char in dic:
                start = max(start, dic[char] + 1)
            
            length = max(length, i - start + 1)
            dic[char] = i
        
        return length

        