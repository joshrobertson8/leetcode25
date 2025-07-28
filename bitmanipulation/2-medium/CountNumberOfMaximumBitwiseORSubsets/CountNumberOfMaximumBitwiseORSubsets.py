class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        totalMax = 0
        count = 0
        
        for mask in range(1 << n): 
            curMax = 0 
            for i in range(n): 

                if mask & (1 << i): 
                    curMax |= nums[i]

            if curMax > totalMax: 
                totalMax = curMax
                count = 1

            elif curMax == totalMax: 
                count +=1 

        return count


if __name__ == "__main__":
    # Example 1
    nums1 = [3, 1]
    print("Test 1 Output:", Solution().countMaxOrSubsets(nums1))  # Expected: 2

    # Example 2
    nums2 = [2, 2, 2]
    print("Test 2 Output:", Solution().countMaxOrSubsets(nums2))  # Expected: 7

    # Example 3
    nums3 = [3, 2, 1, 5]
    print("Test 3 Output:", Solution().countMaxOrSubsets(nums3))  # Expected: 6
