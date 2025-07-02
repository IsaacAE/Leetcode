class Solution(object):
    def isPalindrome(self, x):
        number = str(x) 
        mid = int(len(number)/2)

        for i in range(mid):
            if number[i] != number[(len(number)-i-1)]:
                return False
        
        return True
        