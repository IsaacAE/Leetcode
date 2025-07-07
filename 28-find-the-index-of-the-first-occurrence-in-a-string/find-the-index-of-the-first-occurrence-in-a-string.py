class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+1] == needle[0:1]:
                j = 0
                k = i
                while j < len(needle):
                    
                    if needle[j:j+1] == haystack[k:k+1]:
                        j+=1
                        k+=1
                    else:
                        j+=1
                if k-i == len(needle):
                    return i
        return -1


        