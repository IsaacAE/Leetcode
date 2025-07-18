class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        i = len(a)-1
        j = len(b)-1
        carry = 0
        word = ""

        while i >= 0 and j >=0:
            add = int(a[i]) + int(b[j]) + carry
            val = add % 2
            carry = add // 2
            word += str(val)
            i -= 1
            j-=1

        while i >= 0:
            add = int(a[i]) + carry
            val = add % 2
            carry = add // 2
            word += str(val)
            i -= 1
        
        while j >=0:
            add = int(b[j]) + carry
            val = add % 2
            carry = add // 2
            word += str(val)
            j-=1

        if carry == 1:
            word += "1"
        

        return word[::-1]