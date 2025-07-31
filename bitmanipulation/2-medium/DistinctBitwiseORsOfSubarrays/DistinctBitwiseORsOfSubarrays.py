# Solution for Distinct Bitwise ORs of Subarrays

class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = set()
        previous = set()

        for num in arr: 

            current = {num}

            for val in previous: 

                current.add( val | num )
            
            result.update(current)
            previous = current
            
        return len(result)
    



    
if __name__ == "__main__":
    # Example 1
    arr1 = [0]
    print("Test 1 Output:", Solution().subarrayBitwiseORs(arr1))  # Expected: 1

    # Example 2
    arr2 = [1,1,2]
    print("Test 2 Output:", Solution().subarrayBitwiseORs(arr2))  # Expected: 3

    # Example 3
    arr3 = [1,2,4]
    print("Test 3 Output:", Solution().subarrayBitwiseORs(arr3))  # Expected: 6
