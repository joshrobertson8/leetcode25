# Solution for 904. Fruit Into Baskets

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        basket = {}
        base = 0 
        maxWindow = 0

        for idx, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            while len(basket) > 2:
                leftFruit = fruits[base]

                basket[leftFruit] -= 1

                if basket[leftFruit] == 0:
                    del basket[leftFruit]

                base += 1

            maxWindow = max(maxWindow, idx - base + 1)

        return maxWindow
            

if __name__ == "__main__":
    # Example 1
    fruits1 = [1,2,1]
    print("Test 1 Output:", Solution().totalFruit(fruits1))  # Expected: 3

    # Example 2
    fruits2 = [0,1,2,2]
    print("Test 2 Output:", Solution().totalFruit(fruits2))  # Expected: 3

    # Example 3
    fruits3 = [1,2,3,2,2]
    print("Test 3 Output:", Solution().totalFruit(fruits3))  # Expected: 4

    # Example 4
    fruits4 = [3,3,3,1,2,1,1,2,3,3,4]
    print("Test 4 Output:", Solution().totalFruit(fruits4))  # Expected: 5
