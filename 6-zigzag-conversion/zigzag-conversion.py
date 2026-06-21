class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Optimización 1: Salida anticipada ampliada
        if numRows <= 1:
            return s
        
        subs = [""] * numRows
        k = 0
        step = 1
        
        for letter in s:
            subs[k] += letter
            
            if k == 0:
                step = 1
            elif k == numRows - 1:
                step = -1
                
            k += step
            
        return "".join(subs)