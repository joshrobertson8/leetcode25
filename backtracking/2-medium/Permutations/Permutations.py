class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(curr): 
            if len(curr) == len(nums): 
                res.append(curr[:])
                return
            
            for num in nums: 
                if num not in curr: 
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
                    
        backtrack([])
        return res

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([0,1], [[0,1],[1,0]]),
        ([1], [[1]]),
        ([1,2], [[1,2],[2,1]]),
        ([2,3,4], [[2,3,4],[2,4,3],[3,2,4],[3,4,2],[4,2,3],[4,3,2]])
    ]
    for nums, expected in tests:
        result = sol.permute(nums)
        print(f"Input: {nums}")
        print("Output:", result)
        print("Expected:", expected)
        print("Correct:", sorted(result) == sorted(expected))
        print()
