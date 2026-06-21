class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        
        def search_palindrome(i, j, sub:str):
            left = i
            right = j
            while left >= 0 and right < len(sub) and sub[left] == sub[right]:
                left-=1
                right+=1

            length = right-left
            return [length, left+1, right-1]

        palindrome = s[:1]

        for i in range(0,len(s)):
            odd = search_palindrome(i,i,s)
            even = search_palindrome(i,i+1,s)
            if odd[0]> even[0]:
                res = odd
            else:
                res = even

            if res[0] > len(palindrome):
                palindrome = s[res[1]:res[2]+1]
        return palindrome
        