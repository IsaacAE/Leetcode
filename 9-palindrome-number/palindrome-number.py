class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        number = str(x)
        n = len(number)
        mid = int(n/2)
        n1 = number[0:mid]
        if n % 2 != 0:
            mid = mid+1

        
        n2 = ''
        for i in range(n - 1, mid-1, -1):
            n2 += number[i]
    

        if n1 == n2:
            return True

        return False
            