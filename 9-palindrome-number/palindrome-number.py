class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        number = str(x)
        n = len(number)
        mid = int(n/2)

        for i in range(mid):
            if number[i] != number[(n-i-1)]:
                
                return False
        
        return True
        