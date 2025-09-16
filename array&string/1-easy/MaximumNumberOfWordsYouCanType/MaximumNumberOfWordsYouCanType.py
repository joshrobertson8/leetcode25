class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        seen = set(brokenLetters)
        words = text.split(" ")
        count = 0 

        for word in words: 
            for char in word:
                if char in seen:
                    count +=1
                    break
        return len(words) - count


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: Example 1
    text1 = "hello world"
    broken1 = "ad"
    result1 = sol.canBeTypedWords(text1, broken1)
    print(f"Test 1: text='{text1}', brokenLetters='{broken1}' -> {result1} (expected: 1)")
    
    # Test case 2: Example 2
    text2 = "leet code"
    broken2 = "lt"
    result2 = sol.canBeTypedWords(text2, broken2)
    print(f"Test 2: text='{text2}', brokenLetters='{broken2}' -> {result2} (expected: 1)")
    
    # Test case 3: Example 3
    text3 = "leet code"
    broken3 = "e"
    result3 = sol.canBeTypedWords(text3, broken3)
    print(f"Test 3: text='{text3}', brokenLetters='{broken3}' -> {result3} (expected: 0)")
    
    # Additional test case: No broken letters
    text4 = "hello world"
    broken4 = ""
    result4 = sol.canBeTypedWords(text4, broken4)
    print(f"Test 4: text='{text4}', brokenLetters='{broken4}' -> {result4} (expected: 2)")
    
    # Additional test case: All letters broken
    text5 = "abc"
    broken5 = "abc"
    result5 = sol.canBeTypedWords(text5, broken5)
    print(f"Test 5: text='{text5}', brokenLetters='{broken5}' -> {result5} (expected: 0)")