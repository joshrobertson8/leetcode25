from collections import Counter

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        occurance = Counter(str(n))

        for i in range(30): 
            if occurance == Counter(str(2 ** i)): 
                return True
        return False
