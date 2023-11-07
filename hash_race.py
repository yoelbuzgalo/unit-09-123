def hash_first_char(a_string):
    """
    This returns an ASCII value of the first character in the string.
    """
    if len(a_string) > 0:
        return ord(a_string[0]) # Returns the ASCII value of the first character in string if length is more than 1
    
    return 0 # Returns 0 if the string is empty

def hash_sum(a_string):
    """
    This returns a sum of ASCII values in any given string
    """

    # Guard clause to check if a_string is empty, if it is - immediately return with a 0
    if len(a_string) == 0:
        return 0
    
    # Loops over every character in a string and adds it to the sum,
    sum = 0
    for ch in a_string:
        ascii_val = ord(ch)
        sum += ascii_val
    
    return sum

def main():
    some_string = "abc"
    print(hash_sum(some_string))

if __name__ == "__main__":
    main()