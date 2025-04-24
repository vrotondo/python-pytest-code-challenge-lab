"""
Test suite for the longest palindromic substring function.
This follows TDD (Test-Driven Development) approach.
"""

import pytest
from lib.palindrome import longest_palindromic_substring

def test_basic_palindrome():
    """Test basic palindromes that are provided in the examples."""
    # Test case: "babad" should return "bab" or "aba"
    result = longest_palindromic_substring("babad")
    assert result == "bab" or result == "aba"
    
    # Test case: "cbbd" should return "bb"
    assert longest_palindromic_substring("cbbd") == "bb"
    
    # Test case: "racecar" should return "racecar"
    assert longest_palindromic_substring("racecar") == "racecar"

def test_single_character():
    """Test a string with a single character."""
    # A single character is always a palindrome
    assert longest_palindromic_substring("a") == "a"

def test_two_characters():
    """Test a string with two different characters."""
    # When there's no palindrome longer than 1 character, return any single character
    result = longest_palindromic_substring("ac")
    assert result == "a" or result == "c"

def test_empty_string():
    """Test an empty string."""
    # An empty string should return an empty string
    assert longest_palindromic_substring("") == ""

def test_no_palindrome_longer_than_one():
    """Test a string with no palindrome longer than one character."""
    # String with all different characters
    result = longest_palindromic_substring("abcdefg")
    assert len(result) == 1  # Any single character is valid

def test_long_palindrome():
    """Test a string with a very long palindrome."""
    long_string = "a" * 500 + "b" + "a" * 500
    assert longest_palindromic_substring(long_string) == long_string

def test_multiple_palindromes():
    """Test a string with multiple palindromes of different lengths."""
    # Should return the longest one
    assert longest_palindromic_substring("abbacabba") == "abba"  # Not "cabba"

def test_palindrome_at_start():
    """Test a string with the longest palindrome at the start."""
    assert longest_palindromic_substring("abbaxy") == "abba"

def test_palindrome_at_end():
    """Test a string with the longest palindrome at the end."""
    assert longest_palindromic_substring("xyabba") == "abba"

def test_palindrome_with_special_characters():
    """Test a string with special characters."""
    assert longest_palindromic_substring("a#a") == "a#a"

def test_case_sensitivity():
    """Test that the function is case-sensitive."""
    assert longest_palindromic_substring("Abba") != "abba"
    # The longest palindrome would be a single character
    result = longest_palindromic_substring("Abba")
    assert len(result) == 1

def test_maximum_length():
    """Test a string with length at the upper constraint (1000 characters)."""
    long_string = "a" * 1000
    assert longest_palindromic_substring(long_string) == long_string