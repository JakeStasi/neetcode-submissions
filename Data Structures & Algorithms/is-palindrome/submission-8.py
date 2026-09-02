class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two pointer approach with left and right pointers
        # Removes all puncation and non characters and numbers
        s = ''.join(char for char in s if char.isalnum()).lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1 
        return True
