class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]] 
        for start, end in intervals[1:]: 
            lastEnd = merged[-1][1]
            if start <= lastEnd: 
                merged[-1][1] = max(lastEnd, end)
            else: 
                merged.append([start, end])
        return merged

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[4,7],[1,4]], [[1,7]]),
        ([[1,4],[2,3]], [[1,4]]),
        ([[1,4]], [[1,4]])
    ]
    for intervals, expected in tests:
        result = sol.merge([list(i) for i in intervals])
        print(f"Input: {intervals}")
        print("Output:", result)
        print("Expected:", expected)
        print("Correct:", result == expected)
        print()
