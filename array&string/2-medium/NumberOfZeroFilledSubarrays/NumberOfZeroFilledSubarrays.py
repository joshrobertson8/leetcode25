class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        answer = 0 

        for num in nums:

            if num == 0: 
                count += 1
            else: 
                count = 0
            answer += count
            
        return answer


if __name__ == "__main__":
    # Example 1
    nums1 = [1,3,0,0,2,0,0,4]
    print("Test 1 Output:", Solution().zeroFilledSubarray(nums1))  # Expected: 6

    # Example 2
    nums2 = [0,0,0,2,0,0]
    print("Test 2 Output:", Solution().zeroFilledSubarray(nums2))  # Expected: 9

    # Example 3
    nums3 = [2,10,2019]
    print("Test 3 Output:", Solution().zeroFilledSubarray(nums3))  # Expected: 0

    # Additional cases
    nums4 = [0,0,0,0]
    print("Test 4 Output:", Solution().zeroFilledSubarray(nums4))  # Expected: 10

    nums5 = [1,2,3,4]
    print("Test 5 Output:", Solution().zeroFilledSubarray(nums5))  # Expected: 0
