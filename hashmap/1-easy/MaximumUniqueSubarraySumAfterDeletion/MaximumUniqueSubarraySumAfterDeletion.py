class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        maxSum = 0

        for num in nums: 

            if num > 0 and num not in seen:
                seen.add(num)
                maxSum += num

        if len(seen) == 0:
            return max(nums)
        
        return maxSum
            


    
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 2, 3, 4, 5]
    print("Test 1 Output:", Solution().maximumUniqueSubarray(nums1))  # Expected: 15

    # Example 2
    nums2 = [1, 1, 0, 1, 1]
    print("Test 2 Output:", Solution().maximumUniqueSubarray(nums2))  # Expected: 1

    # Example 3
    nums3 = [1, 2, -1, -2, 1, 0, -1]
    print("Test 3 Output:", Solution().maximumUniqueSubarray(nums3))  # Expected: 3

    nums4 = [-100, -50]
    print("Test 4 Output:", Solution().maximumUniqueSubarray(nums4))  # Expected: -50