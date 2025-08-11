class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7

        # Build list of powers of two that sum to n
        powers = []
        bit = 1
        while n:
            if n & 1:
                powers.append(bit)
            bit <<= 1
            n >>= 1

        # Process queries by direct multiplication over the range
        res = []
        for l, r in queries:
            product = 1
            for i in range(l, r + 1):
                product = (product * powers[i]) % MOD
            res.append(product)

        return res
