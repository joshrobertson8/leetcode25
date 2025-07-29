class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maxOrFromIndex = [0] * len(nums)
        curOr = 0 

        for i in range(len(nums) - 1, -1, -1): 
            curOr |= nums[i]
            maxOrFromIndex[i] = curOr

        
        result = []

        for i in range(len(nums)): 
            target = maxOrFromIndex[i]
            cur = 0 
            count = 0

            for j in range(i, len(nums)): 

                cur |= nums[j]
                count += 1
                
                if cur == target: 
                    break

            result.append(count)

        return result






if __name__ == "__main__":
    # Example 1
    nums1 = [1,0,2,1,3]
    print("Test 1 Output:", Solution().smallestSubarrays(nums1))  # Expected: [3,3,2,2,1]

    # Example 2
    nums2 = [1,2]
    print("Test 2 Output:", Solution().smallestSubarrays(nums2))  # Expected: [2,1]
