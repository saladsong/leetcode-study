class Solution:
    def intToRoman(self, num: int) -> str:
        res = []

        while num > 0:
            thou = 0
            if num >= 1000:
                thou = num // 1000
            num -= thou*1000
            res.append(thou*'M')
                        
            if num >= 900:
                num -= 900
                res.append('CM')
            
            if num >= 500:
                num -= 500
                res.append('D')
                
            if num >= 400:
                num -= 400
                res.append('CD')
            
            hund = 0
            if num >= 100:
                hund = num // 100
            num -= hund*100
            res.append(hund*'C')
                
            if num >= 90:
                num -= 90
                res.append('XC')
            
            if num >= 50:
                num -= 50
                res.append('L')
                
            if num >= 40:
                num -= 40
                res.append('XL')
                
            ten = 0
            if num >= 10:
                ten = num // 10
            num -= ten*10
            res.append(ten*'X')
            
            if num >= 9:
                num -= 9
                res.append('IX')
            
            if num >= 5:
                num -= 5
                res.append('V')
                
            if num >= 4:
                num -= 4
                res.append('IV')
            
            else:
                res.append(num*'I')
                
            int_res = ''
            print(int_res.join(res))
            
            return int_res.join(res)
