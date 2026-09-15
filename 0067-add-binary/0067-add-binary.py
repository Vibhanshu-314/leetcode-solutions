class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a = int(a)
        b = int(b)
        
        result = []
        carry = 0
        
        while a or b:
        
            if a:
                a_last = a % 10
            else:
                a_last = 0
        
            if b:
                b_last = b % 10
            else:
                b_last = 0
        
            if a_last == 1 and b_last == 1 and carry == 0:
                result.append(0)
                carry = 1
        
            elif a_last == 0 and b_last == 0 and carry == 0:
                result.append(0)
                carry = 0
        
            elif a_last == 1 and b_last == 1 and carry == 1:
                result.append(1)
                carry = 1
        
            elif a_last == 0 and b_last == 0 and carry == 1:
                result.append(1)
                carry = 0
        
            elif (a_last == 0 or b_last == 0) and carry == 0:
                result.append(1)
                carry = 0
        
            elif (a_last == 0 or b_last == 0) and carry == 1:
                result.append(0)
                carry = 1
        
            a = a // 10
            b = b // 10
        
        if carry:
            result.append(1)
        
        result.reverse()
        if not result:
            return "0"
        return "".join(map(str,result))    
             
                