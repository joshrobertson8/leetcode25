# Solution for 70. Climbing Stairs

class ClimbingStairs(object):
    
    def bruteForce(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1: 
            return 1
        
        if n == 2: 
            return 2
        
        return self.bruteForce(n - 1) + self.bruteForce(n - 2)
    
    def topDownDP(self, n): 
        #keys are steps, values are the amount of ways to get there
        memo = {1:1, 2:2}

        def dp(n): 
            if n in memo: 
                return memo[n]
                
            else: 
                memo[n] = dp(n - 1) + dp(n - 2)
                return memo[n]
        return dp(n)
    
    def bottomUpDP(self, n): 

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n): 

            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1]
                
        
if __name__ == "__main__":
    # Test cases for bruteForce
    n1 = 2
    print("bruteForce Test 1 Output:", ClimbingStairs().bruteForce(n1))  # Expected: 2
    n2 = 3
    print("bruteForce Test 2 Output:", ClimbingStairs().bruteForce(n2))  # Expected: 3

    # Test cases for topDownDP
    n3 = 2
    print("topDownDP Test 1 Output:", ClimbingStairs().topDownDP(n3))  # Expected: 2
    n4 = 3
    print("topDownDP Test 2 Output:", ClimbingStairs().topDownDP(n4))  # Expected: 3
    n5 = 5
    print("topDownDP Test 3 Output:", ClimbingStairs().topDownDP(n5))  # Expected: 8
    n6 = 10
    print("topDownDP Test 4 Output:", ClimbingStairs().topDownDP(n6))  # Expected: 89

    # Test cases for bottomUpDP
    n7 = 2
    print("bottomUpDP Test 1 Output:", ClimbingStairs().bottomUpDP(n7))  # Expected: 2
    n8 = 3
    print("bottomUpDP Test 2 Output:", ClimbingStairs().bottomUpDP(n8))  # Expected: 3
    n9 = 5
    print("bottomUpDP Test 3 Output:", ClimbingStairs().bottomUpDP(n9))  # Expected: 8
    n10 = 10
    print("bottomUpDP Test 4 Output:", ClimbingStairs().bottomUpDP(n10))  # Expected: 89
