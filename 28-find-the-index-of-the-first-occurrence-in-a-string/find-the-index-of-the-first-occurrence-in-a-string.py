class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
            
        return -1


        