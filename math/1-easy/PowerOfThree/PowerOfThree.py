class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n /= 3

        return n == 1
    


if __name__ == "__main__":
    # Example 1
    n1 = 27
    print("Test 1 Output:", Solution().isPowerOfThree(n1))  # Expected: True

    # Example 2
    n2 = 0
    print("Test 2 Output:", Solution().isPowerOfThree(n2))  # Expected: False

    # Example 3
    n3 = -1
    print("Test 3 Output:", Solution().isPowerOfThree(n3))  # Expected: False

    # Additional cases
    n4 = 1
    print("Test 4 Output:", Solution().isPowerOfThree(n4))  # Expected: True

    n5 = 9
    print("Test 5 Output:", Solution().isPowerOfThree(n5))  # Expected: True

    n6 = 10
    print("Test 6 Output:", Solution().isPowerOfThree(n6))  # Expected: False
