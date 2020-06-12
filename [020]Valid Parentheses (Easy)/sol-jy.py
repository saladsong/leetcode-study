class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {')':'(',
                     '}':'{', 
                     ']':'['}
        stack = []
        
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last = stack[-1]
                if pair_dict[char] == last:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
