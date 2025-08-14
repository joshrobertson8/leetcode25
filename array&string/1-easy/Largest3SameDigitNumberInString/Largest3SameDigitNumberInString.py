class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        maxGood = 0

        for i in range(1, len(num) - 1):
            good = 0

            if num[i - 1] == num[i] == num[i + 1]:
                good = num[i]
                maxGood = max(maxGood, good)
            

        return maxGood * 3 if maxGood != 0 else ""


if __name__ == "__main__":
    # Example 1
    num1 = "6777133339"
    print("Test 1 Output:", Solution().largestGoodInteger(num1))  # Expected: "777"

    # Example 2
    num2 = "2300019"
    print("Test 2 Output:", Solution().largestGoodInteger(num2))  # Expected: "000"

    # Example 3
    num3 = "42352338"
    print("Test 3 Output:", Solution().largestGoodInteger(num3))  # Expected: ""

    # Additional cases
    num4 = "123456789"
    print("Test 4 Output:", Solution().largestGoodInteger(num4))  # Expected: ""

    num5 = "999111222333444555666777888000"
    print("Test 5 Output:", Solution().largestGoodInteger(num5))  # Expected: "999"
