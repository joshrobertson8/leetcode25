# Solution for 3477. Fruits Into Baskets II

class Solution(object):
    def unplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        res = 0 
        n = len(baskets)

        for fruit in fruits:
            unset = 1

            for j in range(n):

                if fruit <= baskets[j]: 
                    unset = 0
                    baskets[j] = 0
                    break
            res += unset
                
        return res

if __name__ == "__main__":
    # Example 1
    fruits1 = [4,2,5]
    baskets1 = [3,5,4]
    print("Test 1 Output:", Solution().unplacedFruits(fruits1, baskets1))  # Expected: 1

    # Example 2
    fruits2 = [3,6,1]
    baskets2 = [6,4,7]
    print("Test 2 Output:", Solution().unplacedFruits(fruits2, baskets2))  # Expected: 0
