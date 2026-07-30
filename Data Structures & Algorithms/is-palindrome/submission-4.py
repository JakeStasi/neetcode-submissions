class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []

        for x in s:
            if x.isalnum():
                word.append(x)
        
        left = 0
        right = len(word) - 1

        while left < right:
            
            if word[left].lower() != word[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True
