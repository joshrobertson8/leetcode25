class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("No lemon, no melon", True),
        ("12321", True),
        ("12345", False)
    ]
    for s, expected in tests:
        result = sol.isPalindrome(s)
        print(f"Input: {s!r} | Output: {result} | Expected: {expected}")
