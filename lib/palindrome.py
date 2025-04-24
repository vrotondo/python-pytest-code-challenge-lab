def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    
    Args:
        s (str): The input string
        
    Returns:
        str: The longest palindromic substring of s
        
    Time Complexity: O(n^2) where n is the length of the string
    Space Complexity: O(1)
    """
    # Handle edge cases
    if not s:
        return ""
    
    if len(s) < 2:
        return s
    
    start = 0
    max_len = 1

    # Helper function to expand around center
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the indices of the palindrome (not the length)
        # We need to add 1 to left and subtract 1 from right because
        # the while loop exits after the condition fails
        return left + 1, right - 1
    
    # Check each position as a potential center
    for i in range(len(s)):
        # Odd length palindrome (single character center)
        left1, right1 = expand_around_center(i, i)
        len1 = right1 - left1 + 1
        
        # Even length palindrome (between two characters)
        left2, right2 = expand_around_center(i, i + 1)
        len2 = right2 - left2 + 1
        
        # Find the maximum length
        if len1 > max_len:
            max_len = len1
            start = left1
            
        if len2 > max_len:
            max_len = len2
            start = left2
    
    return s[start:start + max_len]