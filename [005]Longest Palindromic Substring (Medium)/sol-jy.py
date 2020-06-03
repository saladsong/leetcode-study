class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        
        tmp, idx = {2:[], 3:[]}, {2:[], 3:[]}
        
        # even case
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                tmp[2].append(2*s[i])
                idx[2].append(i)
        if len(tmp[2]) == 0:
            del tmp[2]
            del idx[2]
    
        # odd case
        for i in range(1,len(s)-1):
            if s[i-1] == s[i+1]:
                tmp[3].append(s[i-1:i+2])
                idx[3].append(i)
        if len(tmp[3]) == 0:
            del tmp[3]
            del idx[3]
        
        # even case
        #print('even; ', tmp, idx)
        k = 1
        try:
            while len(tmp[2*k]) > 0:
                tmp[2*(k+1)], idx[2*(k+1)] = [], []
                for i, ch in enumerate(idx[2*k]):
                    #print(ch-1, ch+2*k)
                    try:
                        if (ch-1) >= 0 and s[ch-1] == s[ch+2*k]:
                            tmp[2*(k+1)].append(s[ch-1:ch+2*k+1])
                            idx[2*(k+1)].append(ch-1)
                    except IndexError:
                        pass
                k += 1
        except KeyError:
            pass
        
        # odd case
        #print('odd; ', tmp, idx)
        k = 1
        try:
            while len(tmp[2*k+1]) > 0:
                tmp[2*k+3], idx[2*k+3] = [], []
                for i, ch in enumerate(idx[2*k+1]):
                    #print(ch-(k+1), ch+(k+1))
                    try:
                        if ch-(k+1) >= 0 and s[ch-(k+1)] == s[ch+(k+1)]:
                            tmp[2*k+3].append(s[ch-(k+1):ch+(k+2)])
                            idx[2*k+3].append(ch)
                    except IndexError:
                        pass
                k += 1

        except KeyError:
            pass
        
    
        #print(tmp, idx)
        if len(tmp.keys()) == 0:
            return s[0]
        else:
            for i in idx.keys():
                if len(idx[i]) == 0:
                    del tmp[i]
            res = max(tmp.keys())
            print(res)
            return tmp[res][0]
