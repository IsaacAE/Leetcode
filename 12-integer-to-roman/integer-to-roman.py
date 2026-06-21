class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numbers = {
        # Miles
        3000: "MMM",
        2000: "MM",
        1000: "M",
        
        # Centenas
        900: "CM",
        800: "DCCC",
        700: "DCC",
        600: "DC",
        500: "D",
        400: "CD",
        300: "CCC",
        200: "CC",
        100: "C",
        
        # Decenas
        90: "XC",
        80: "LXXX",
        70: "LXX",
        60: "LX",
        50: "L",
        40: "XL",
        30: "XXX",
        20: "XX",
        10: "X",
        
        # Unidades
        9: "IX",
        8: "VIII",
        7: "VII",
        6: "VI",
        5: "V",
        4: "IV",
        3: "III",
        2: "II",
        1: "I",
        0:''
    }
        roman_num=''
        def get_pos_val(number: int) -> list:
            values = list()
            numC = abs(number)
            
            mult = 1 
            
            while numC > 0:
                digit = numC % 10
            
                val_pos = digit * mult
                
                values.insert(0,val_pos)
                
                numC = numC // 10
                
                mult *= 10 
                
            return values

        translate = get_pos_val(num)
        for n in translate:
            roman_num+= roman_numbers[n]

        return roman_num


        