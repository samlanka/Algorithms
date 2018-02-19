
#Author: Sameera Lanka

def isPalindrome(string):
    """Input: string
       Output: (bool) True if string is palindrome,
                    False otherwise"""
  if len(string) == 1 or len(string) == 0:
    return True
  else:
    if string[0] == string[-1]:
      return isPalindrome(string[1:-1])
    else:
      return False
