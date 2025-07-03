class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = min(strs, key=len)
       
        i = len(word)
        while i != -1:
            correct = True
            prefix = word[:i]
            for s in strs:
                if prefix != s[:i]:
                    correct = False
            
            if(correct):
                return prefix
            else:
                i -=1
        

        