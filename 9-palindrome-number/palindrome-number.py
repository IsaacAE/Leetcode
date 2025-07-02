class Solution(object):
    def isPalindrome(self, x):
        number = str(x)
        n = len(number)
        mid = int(n/2)

        for i in range(mid):
            if number[i] != number[(n-i-1)]:
                
                return False
        
        return True
        