class Solution:
    def myAtoi(self, strr: str) -> int:
        s = ""
        for i in range(len(strr)):
            if strr[i] != " ":
                s = strr[i:]
                break
        print(s)
        
        if len(s) == 0:
            return 0
        
        ss = []
        tmp = 0
        if s[0] == '-':
            tmp = s[0]
            ss.append(str(tmp))
        elif s[0] == '+':
            pass
        else:
            try:
                tmp = int(s[0])
                ss.append(str(tmp))
            except ValueError:
                return 0     
        
        for i in range(1,len(s)):
            try:
                tmp = int(s[i])
            except ValueError:
                break
            ss.append(str(tmp))
        print(ss)
        res = "".join(ss)

        try:
            res = int(res)
            print(res)
            
            INT_MIN = -2**31
            INT_MAX = 2**31-1
            if res < INT_MIN:
                res = INT_MIN
            elif res > INT_MAX:
                res = INT_MAX
        except ValueError:
            return 0
         
        return res
