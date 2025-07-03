class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"Z":0,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
      
        prev = 'Z'
        value = 0
        for c in s:
            current_v = roman.get(c)
            prev_v = roman.get(prev)
            if prev_v < current_v:
                value -= 2*prev_v
            prev = c
            value += current_v
            
        return value

        