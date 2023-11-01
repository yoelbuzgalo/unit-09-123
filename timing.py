"""
A Python module that provides a timing function that can be used to time how
long it takes to execute some other function.

@author GCCIS Faculty
"""
import time

def time_function(function, *args):
    """
    Uses the provided parameters as arguments when executing the given function
    and times how long it takes to execute.

    *args may be zero or more parameters.
    """
    print("timing", function.__name__)
    start = time.perf_counter()
    result = function(*args)
    end = time.perf_counter()
    print("  elapsed time:", (end - start))
    return result

def __test_function(a, b, c):
    """
    An example function that is used to demonstrat the time_function works.
    """
    print(a, b, c)
    return "foobar"

def __main():
    """
    Provides an example of how to use time_function.
    """
    result = time_function(__test_function, "a", 1, False)
    print(result)

if __name__ == "__main__":
    __main()
