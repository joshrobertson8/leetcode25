class Solution(object):
    def countHillsAndValleys(self, nums):
        vallys = 0 
        hills = 0
        i = 1

        while i < len(nums):
            
            cur = nums[i]

            left = i - 1
            while left > 0 and nums[left] == cur: 
                left -=1
            
            right = i + 1
            while right < len(nums) and nums[right] == cur:
                right += 1

            
            if left >= 0 and right < len(nums):
                if cur > nums[right] and cur > nums[left]:
                    hills +=1
                
                elif cur < nums[right] and cur < nums[left]:
                    vallys += 1

            i = right 

        return hills + vallys


if __name__ == "__main__":
    # Example 1
    nums1 = [2,4,1,1,6,5]
    print("Test 1 Output:", Solution().countHillsAndValleys(nums1))  # Expected: 3

    # Example 2
    nums2 = [6,6,5,5,4,1]
    print("Test 2 Output:", Solution().countHillsAndValleys(nums2))  # Expected: 0

    # Tricky Case 1: Flat plateau
    nums3 = [3,3,3,3,3]
    print("Test 3 Output:", Solution().countHillsAndValleys(nums3))  # Expected: 0

    # Tricky Case 2: Plateau hill
    nums4 = [1,2,2,2,1]
    print("Test 4 Output:", Solution().countHillsAndValleys(nums4))  # Expected: 1

    # Tricky Case 3: Plateau valley
    nums5 = [5,3,3,3,6]
    print("Test 5 Output:", Solution().countHillsAndValleys(nums5))  # Expected: 1

    # Tricky Case 4: Zigzag with duplicates
    nums6 = [1,3,3,1,2,2,4,4,2]
    print("Test 6 Output:", Solution().countHillsAndValleys(nums6))  # Expected: 3

    # Tricky Case 5: Smallest allowed array
    nums7 = [1,2,1]
    print("Test 7 Output:", Solution().countHillsAndValleys(nums7))  # Expected: 1

    # Tricky Case 6: Edge plateau
    nums8 = [2,2,3,2,2]
    print("Test 8 Output:", Solution().countHillsAndValleys(nums8))  # Expected: 1
