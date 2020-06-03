class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_len = find_minlen(strs)
        
        idx = 0
        while idx < min_len:
            char = strs[0][idx]
            
            cnt = 0
            for item in strs:
                if item[idx] == char:
                    cnt += 1
            if cnt == len(strs):
                res += char
                idx += 1
            else:
                break
            
        print(res)
        
        return res
       
def find_minlen(lst):
    if len(lst) > 0:
        min_len = len(lst[0])
        for item in lst:
            if len(item) < min_len:
                min_len = len(item)
    else:
        min_len = 0
    return min_len
