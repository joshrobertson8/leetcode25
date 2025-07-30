# Solution for Longest Subarray With Maximum Bitwise AND

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = max(nums)
        current = 0 
        longest = 0

        for num in nums: 

            if num == maxVal:
                current += 1

            else:
                current = 0
            
            longest = max(longest, current)

        return longest 

if __name__ == "__main__":
    # Example 1
    nums1 = [1,2,3,3,2,2]
    print("Test 1 Output:", Solution().longestSubarray(nums1))  # Expected: 2

    # Example 2
    nums2 = [1,2,3,4]
    print("Test 2 Output:", Solution().longestSubarray(nums2))  # Expected: 1
