class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        strNum = str(num)
        res = ''
        
        for i, j in enumerate(strNum): 

            if j == '6':
                res += '9' + strNum[i + 1:]
                break

            else: 
                res += '9'
            
        return int(res)


if __name__ == "__main__":
    # Example 1
    num1 = 9669
    print("Test 1 Output:", Solution().maximum69Number(num1))  # Expected: 9969

    # Example 2
    num2 = 9996
    print("Test 2 Output:", Solution().maximum69Number(num2))  # Expected: 9999

    # Example 3
    num3 = 9999
    print("Test 3 Output:", Solution().maximum69Number(num3))  # Expected: 9999

    # Additional cases
    num4 = 6699
    print("Test 4 Output:", Solution().maximum69Number(num4))  # Expected: 9699

    num5 = 6969
    print("Test 5 Output:", Solution().maximum69Number(num5))  # Expected: 9969