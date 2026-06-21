class Solution:
    def longestPalindrome(self, s: str) -> str:
        k = len(s)
        palindrome = s[:1]
        while k >= 1:
            sub = s[0:k]
            if len(sub) % 2 == 1:
                i = max(0, (len(sub) - 1) // 2)
                j = min(len(sub) - 1, (len(sub) - 1) // 2)
            else: 
                i = max(0,len(sub)//2-1)
                j = min(len(sub)-1,len(sub)//2)
            
            start = i
            end = j
            
            

            while i >= 0 and j < len(sub):
                if sub[i] == sub[j]:
                    if j - i >= len(palindrome):
                        palindrome = sub[i:j+1]
                else:
                    i=-1
                i-=1
                j+=1
            k-=1
        k = 0
        while k < len(s):
            sub = s[k:len(s)]
            if len(sub) % 2 == 1:
                i = max(0, (len(sub) - 1) // 2)
                j = min(len(sub) - 1, (len(sub) - 1) // 2)
            else: 
                i = max(0,len(sub)//2-1)
                j = min(len(sub)-1,len(sub)//2)
            
            start = i
            end = j
            
            

            while i >= 0 and j < len(sub):
                if sub[i] == sub[j]:
                    if j - i >= len(palindrome):
                        palindrome = sub[i:j+1]
                else:
                    i=-1
                i-=1
                j+=1
            k+=1
        return palindrome

        