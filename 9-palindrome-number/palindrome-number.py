class Solution(object):
    def isPalindrome(self, x):
        number = str(x)
        n = len(number)
        mid = int(n/2)
        k = n-1

        for i in range(mid):
            if number[i] != number[(k-i)]:
                
                return False
        
        return True
        