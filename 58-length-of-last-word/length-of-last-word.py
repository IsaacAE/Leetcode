class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        for i in range(len(s)-1,-1, -1):
            if s[i] != " ":
                j = i
                while s[j] != " " and j >=0:
                    word += s[j]
                    j-=1
            
                return len(word)

        return 0
        