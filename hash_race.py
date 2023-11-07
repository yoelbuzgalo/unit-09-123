def hash_first_char(a_string):
    """
    This returns an ASCII value of the first character in the string.
    """
    if len(a_string) > 0:
        return ord(a_string[0]) # Returns the ASCII value of the first character in string if length is more than 1
    
    return 0 # Returns 0 if the string is empty