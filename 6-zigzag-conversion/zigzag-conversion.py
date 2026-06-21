class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        diagonal = False
        subs = [""] * numRows
        k = 0
        for letter in s:
            subs[k]+=letter
            if diagonal:
                k-=1
            else:
                k+=1

            if k == numRows-1 and diagonal==False: 
                diagonal = True
            elif k == numRows-1 and diagonal == True:
                diagonal = False
            elif k == 0 and diagonal == True:
                diagonal = False
        
        return "".join(subs)


        