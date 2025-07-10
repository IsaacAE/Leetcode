class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        word = ""
        length = 0
        i = 0
        while i < len(s):
            char = s[i:i+1]
            r = dic.get(char)
            if r != None:
                dic = {}
                i = r+1
                
                word= ""

            
            elif r == None:
                dic.update({char:i})
                word += char
                if len(word) > length:
                    length = len(word)
                i+=1
        
        return length

        