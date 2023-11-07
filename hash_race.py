import time

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

    length = len(a_string) # Store the length of a given string to improve speed (reduce function calls per iteration)
    
    # Guard clause to check if the string is empty, it will return 0 immediately if it is empty
    if length == 0:
        return 0

    # Loops every character and creates adds to sum w/ hash value based on position and exponents of each letter in string
    sum = 0
    for i in range(length):
        # Formula taken from the instruction
        exponent = length-(i+1) # Exponent value (positional)
        ascii_val = ord(a_string[i]) # Convert iterated character to ascii value
        sum += (ascii_val*(31**exponent)) # Multiply and update for every iteration to the sum variable
    
    return sum

def build_collision_counter(hash_func):
    """
    This function loops over a file, hashes every line and adds to dictionary with with a count of how many hash collissions
    """
    # Initialize a dict
    dict_of_hash = dict()
    number_of_lines = 0

    # Opens the file
    with open("data/long_line_words.txt") as file:
        # Loop through every line in file
        for line in file:
            number_of_lines += 1
            line = line.strip() # Strip for trailing/whitespaces
            hash_code = hash_func(line) # Convert every line with a hash function
            if hash_code in dict_of_hash: # Check if it exists in dict, if it does - add by 1, otherwise create a key of it
                dict_of_hash[hash_code] += 1
            else:
                dict_of_hash[hash_code] = 1
    return dict_of_hash, number_of_lines # Return the dict and number of lines attempted to create key and value pairs.

def get_perf_time(func, *args):
    """
    Helper function that retrieves performance time and also returns the functions' returned value
    """
    start = time.perf_counter() # Get starting time
    value = func(*args) # Call the function, pass any arguments
    end = time.perf_counter() # Get end time

    elapsed = end - start # Calculate the elapsed time
    
    return value, elapsed # Return both values

def hash_test(hash_func, collision_counter):
    """
    This function tests the quality of a given hash function passed to this function
    """

    # Print the name of hash function passed for testing
    print("hash function:", hash_func.__name__)
    collission_counter_value, elapsed_time = get_perf_time(collision_counter, hash_func) # Calls a helper function w/ the collision counter function and the hash function.
    
    collision_dict, number_of_lines = collission_counter_value # Unpack the returned value

    total_hash_keys = len(collision_dict) # Returns how many keys were created in dictionary (total hash output)

    # Initialize count and max variables
    total_collission_count = 0
    max_collission = 0

    # Loops over every hash key in collission dict and retrieves values (collision count)
    for hash_key in collision_dict:
        total_collission_count += (collision_dict[hash_key] - 1) # Updates total collission count

        # Checks if the current collision is higher than previous max collission, if so - updates it
        if (collision_dict[hash_key] - 1) > max_collission: 
            max_collission = (collision_dict[hash_key] - 1)
    
    total_collission_rate = round((100 * (float(total_collission_count)/float(total_hash_keys))), 2) # Gets the percentage based on ratio and rounds to 2 decimals
    spread_rate = round((100 * (float(total_hash_keys)/float(number_of_lines))), 2) # Gets the spread rate percentage based on ratio of hash key outputs to the amount of lines.

    # Print calculated values
    print("total collission rate: ", total_collission_rate, "%", sep="")
    print("maximum collisions:", max_collission)
    print("spread: ", spread_rate, "%", sep="")
    print("speed:", round(elapsed_time, 2), "seconds", end="\n\n")


def main():
    # some_string = "abc"
    # print(hash_sum(some_string))
    # print(hash_positional_sum("abcd"))
    # print(hash_positional_sum("bdca"))
    # print(build_collision_counter(hash_positional_sum))
    hash_test(hash, build_collision_counter)
    hash_test(hash_first_char, build_collision_counter)
    hash_test(hash_sum, build_collision_counter)
    hash_test(hash_positional_sum, build_collision_counter)
    

if __name__ == "__main__":
    main()