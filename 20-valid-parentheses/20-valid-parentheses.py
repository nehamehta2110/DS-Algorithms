class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        output = True
        for i in s:
            if i in ['(','[','{']:
                stck.append(i)
            else:
                if len(stck)==0:
                    return False
                top = stck[-1]
                stck.pop()
                if (top=='(' and i==')') or (top=='[' and i==']') or (top=='{' and i=='}'):
                    output = True
                else:
                    output = False
                if not output:
                    return False
        if len(stck)!=0:
            return False
        return True
                
            
            
        