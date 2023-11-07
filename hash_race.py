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

def hash_positional_sum(a_string):
    
    # Guard clause to check if the string is empty, it will return 0 immediately if it is empty
    if len(a_string) == 0:
        return 0

    # 
    sum = 0
    for i in range(len(a_string)):
        # Formula taken from the instruction
        exponent = len(a_string)-(i+1) # Exponent value (positional)
        ascii_val = ord(a_string[i]) # Convert iterated character to ascii value
        sum += (ascii_val*(31**exponent)) # Multiply and update for every iteration to the sum variable
    
    return sum


def main():
    # some_string = "abc"
    # print(hash_sum(some_string))
    print(hash_positional_sum("abcd"))
    print(hash_positional_sum("bdca"))

if __name__ == "__main__":
    main()