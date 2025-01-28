# String Functions in Python

# 1. String Length
s = "Hello, World!"
print(len(s))

# 2. Convert to Uppercase
print(s.upper())

# 3. Convert to Lowercase
print(s.lower())

# 4. Capitalize First Letter
print(s.capitalize())

# 5. Title Case
print(s.title())

# 6. Swap Case
print(s.swapcase())

# 7. Count Occurrences of a Substring
print(s.count("o"))

# 8. Find Index of Substring
print(s.find("World"))

# 9. Replace a Substring
print(s.replace("World", "Python"))

# 10. Check if String Starts with a Specific Substring
print(s.startswith("Hello"))

# 11. Check if String Ends with a Specific Substring
print(s.endswith("!"))

# 12. Split String into List
print(s.split(","))

# 13. Join List into String
words = ["Python", "is", "awesome"]
print(" ".join(words))

# 14. Remove Leading and Trailing Spaces
s2 = "   Trim Spaces   "
print(s2.strip())

# 15. Check if String Contains Only Digits
num_str = "12345"
print(num_str.isdigit())

# 16. Check if String Contains Only Alphabets
alpha_str = "Python"
print(alpha_str.isalpha())

# 17. Check if String Contains Alphanumeric Characters
alnum_str = "Python123"
print(alnum_str.isalnum())

# 18. Check if String is in Lowercase
print(s.islower())

# 19. Check if String is in Uppercase
print(s.isupper())

# 20. Check if String is Title Case
print(s.istitle())

# 21. Check if String Contains Only Whitespace
space_str = "   "
print(space_str.isspace())

# 22. Center Align String
print(s.center(20, "-"))

# 23. Left Align String
print(s.ljust(20, "-"))

# 24. Right Align String
print(s.rjust(20, "-"))

# 25. Convert Tabs to Spaces
tab_str = "Python\tis\tfun"
print(tab_str.expandtabs(4))
