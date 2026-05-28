from curses.ascii import isalnum


def is_palindrome(word):
    
    left, right = 0, len(word) - 1

    while left < right:
        while left < right and not word[left].isalnum():# skipping non alpha chars
          left += 1

        while left < right and not word[right].isalnum():
          right -= 1
        
        if word[left].lower() != word[right].lower():
            return False
        
        left += 1
        right -= 1
   

    return True
    