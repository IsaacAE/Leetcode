class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
      
        n = len(s)-1
        value = 0
        for i in range(n):
            actual = roman.get(s[i])
            next = roman.get(s[i+1])
            if actual < next:
                value -= actual
            else:
                value +=actual
            
        value += roman.get(s[n])
        
        return value

        