import math

class Solution:
    def generate(self, numRows):
        result = []
        
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                #iCj
                binomial_coefficient = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
                row.append(binomial_coefficient)
            result.append(row)
        
        return result
        
        
