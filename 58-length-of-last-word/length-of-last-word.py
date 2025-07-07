class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        i = len(s)-1
        while i >= 0 and s[i] == " ":
            i-=1

        j = i
        while s[j] != " " and j >=0:
            word += s[j]
            j-=1
            
        return len(word)

        