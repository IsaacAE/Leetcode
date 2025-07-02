class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        number = str(x)
        n = len(number)
        mid = int(n/2)

        n1 = number[0:mid]
        if n % 2 == 0:
            n2 = number[mid:n]
        else: 
            n2 = number[mid+1:n]
        n2 = n2[::-1]
        print(n1)
        print(n2)

        if n1 == n2:
            return True

        return False
            