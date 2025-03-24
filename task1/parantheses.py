class Solution:
    def isValid(self, s):
        pairing={']':'[','}':'{',')':'('}
        array=[]
        for char in s:
            if char in pairing.values():
                array.append(char)
            elif char in pairing.keys():
                if array and array[-1] == pairing[char]:
                   array.pop()
                else:
                    return False
        return not array

