class Solution(object):
    def countMaxOrSubsets(self, nums):
        count = 0
        maxOr = 0 

        for num in nums: 
            maxOr |= num
        
        def backtrack(idx, curOr): 
            nonlocal count, maxOr
            if idx == len(nums):
                if curOr == maxOr: 
                    count += 1
                return 
            backtrack(idx + 1, curOr)
            backtrack(idx + 1, curOr | nums[idx])
        backtrack(0, 0)
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
