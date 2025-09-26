import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),
        ([7,10,4,3,20,15], 3, 10)
    ]
    for nums, k, expected in tests:
        result = sol.findKthLargest(list(nums), k)  # use list(nums) to avoid modifying original
        print(f"Input: nums={nums}, k={k}")
        print("Output:", result)
        print("Expected:", expected)
        print("Correct:", result == expected)
        print()
