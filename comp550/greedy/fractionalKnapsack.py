class Solution:
    def zeroIndexifyIntervals(self, intervals):
        # Convert 1-indexed intervals to 0-indexed
        return [[start - 1, end - 1] for start, end in intervals]
    
    def fractionalKnapsack(self, value, weight, capacity):
        """
        Solve the fractional knapsack problem using greedy approach.
        Items are given as lists of values and weights.
        """
        
        items = sorted(zip(value, weight), key=lambda x: x[0] / x[1], reverse=True)

        totalValue = 0.0

        for val, wt in items: 
            if wt <= capacity: 
                totalValue += val
                capacity -= wt
            
            else: 
                totalValue += val * (capacity / wt)
                break

        return int(totalValue * 100) / 100.0

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: Provided data
    values1 = [64, 111, 58, 168, 98, 192, 142, 129, 214, 205, 240, 243, 127, 190, 150, 216, 221, 242, 242, 123, 215, 237, 113, 93, 202, 187, 71]
    weights1 = [1, 2, 2, 23, 10, 38, 16, 24, 8, 18, 31, 59, 14, 27, 46, 21, 64, 49, 35, 40, 37, 11, 3, 10, 14, 44, 5]
    capacity1 = 31
    result1 = sol.fractionalKnapsack(values1, weights1, capacity1)
    print("Test 1 - Values:", values1)
    print("Weights:", weights1)
    print("Capacity:", capacity1)
    print("Max Value:", result1)
    print()
    
    # Test case 2: Another example
    values2 = [10, 5, 15, 7, 6, 18, 3]
    weights2 = [2, 3, 5, 7, 1, 4, 1]
    capacity2 = 15
    result2 = sol.fractionalKnapsack(values2, weights2, capacity2)
    print("Test 2 - Values:", values2)
    print("Weights:", weights2)
    print("Capacity:", capacity2)
    print("Max Value:", result2)
    print()
    
    # Test case 3: No capacity
    values3 = [10, 20]
    weights3 = [5, 10]
    capacity3 = 0
    result3 = sol.fractionalKnapsack(values3, weights3, capacity3)
    print("Test 3 - Values:", values3)
    print("Weights:", weights3)
    print("Capacity:", capacity3)
    print("Max Value:", result3)
