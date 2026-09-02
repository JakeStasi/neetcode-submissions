class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two pointer approach with left and right pointers
        # Removes all puncation and non characters and numbers
        s = ''.join(char for char in s if char.isalnum()).lower()

        left = 0
        right = len(s) - 1

        # While left and right don't overlap eachother moving from left of the string to the right of the string continue to loop thru
        while left < right:
            # If they arent equal then we know it isnt a palindrome so we can just return False
            if s[left] != s[right]:
                return False
            # If we get to this point then we compared 2 letters lets say "a" and "a"
            # which means we have to continue thru the string to check the rest of the letters
            left +=1
            right -=1 
        return True
