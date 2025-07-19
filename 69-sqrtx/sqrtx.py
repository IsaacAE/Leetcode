class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
            
        start = 0
        end = x
        search = int((start + end) / 2)
        
        while start <= end:
            search = int((start + end) / 2)
            if (search**2) == x:
                return search
            elif (search**2) > x:
                end = search-1
            else:
                start = search+1
                
        if (search**2) > x:
            return search-1
        else:
            return search
            