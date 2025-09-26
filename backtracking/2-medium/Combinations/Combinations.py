class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = [] 

        def backtrack(start, curr): 
            if len(curr) == k: 
                res.append(curr[:])
                return
            for i in range(start, n + 1): 
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop() 
        backtrack(1, [])
        return res

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]),
        (1, 1, [[1]]),
        (5, 3, [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]])
    ]
    for n, k, expected in tests:
        result = sol.combine(n, k)
        print(f"Input: n={n}, k={k}")
        print("Output:", result)
        print("Expected:", expected)
        print("Correct:", sorted(result) == sorted(expected))
        print()
