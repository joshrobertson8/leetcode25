class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        for num1 in range(1, n):

            num2 = n - num1

            if "0" not in str(num1) + str(num2):

                return [num1, num2]
        return []
    

if __name__ == "__main__":
    # Example 1
    n1 = 2
    print("Test 1 Output:", Solution().getNoZeroIntegers(n1))  # Expected: [1, 1]

    # Example 2
    n2 = 11
    print("Test 2 Output:", Solution().getNoZeroIntegers(n2))  # Expected: [2, 9]

    # Additional cases
    n3 = 3
    print("Test 3 Output:", Solution().getNoZeroIntegers(n3))  # Expected: [1, 2]

    n4 = 10
    print("Test 4 Output:", Solution().getNoZeroIntegers(n4))  # Expected: [1, 9]

    n5 = 100
    print("Test 5 Output:", Solution().getNoZeroIntegers(n5))  # Expected: [1, 99]
