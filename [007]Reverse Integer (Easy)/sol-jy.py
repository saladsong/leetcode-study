class Solution:
    def reverse(self, x: int) -> int:
        if x > (2**31-1) or x <= -(2**31):
            return 0
        
        elif x >= 0:
            div, mod = divmod(x,10)
            temp = mod
            while div != 0:  
                div, mod = divmod(div, 10)
                temp = temp * 10 + mod
            if temp > (2**31-1) or temp <= -(2**31):
                return 0
            return temp
                
        else:
            div, mod = divmod(-x,10)
            temp = mod
            while div != 0:  
                div, mod = divmod(div, 10)
                temp = temp * 10 + mod
            if temp > (2**31-1) or temp <= -(2**31):
                return 0
            return temp * (-1)
