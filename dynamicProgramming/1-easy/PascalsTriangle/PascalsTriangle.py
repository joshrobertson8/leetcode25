# Solution for Pascal's Triangle

class Solution(object):
    def pascalsTriangle(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        result = [[1]]

        for i in range(numRows - 1): 
            temp = [0] + result[-1] + [0]
            nextRow = []
            for j in range(len(result[-1]) + 1):
                nextRow.append(temp[j] + temp[j + 1])
            result.append(nextRow)
        return result

if __name__ == "__main__":
    # Example 1
    numRows1 = 5
    print("Test 1 Output:", Solution().pascalsTriangle(numRows1))  # Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    # Example 2
    numRows2 = 1
    print("Test 2 Output:", Solution().pascalsTriangle(numRows2))  # Expected: [[1]]
