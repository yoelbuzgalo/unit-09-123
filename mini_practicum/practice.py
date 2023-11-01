"""
Implement your solution to the mini-practicum here.

YOEL BUZGALO
"""

def increasing_comparator(a, b):
    """
    A comparator function that returns True if a is less than or equal to b, 
    and False otherwise.
    """
    return a <= b

def decreasing_comparator(a, b):
    """
    This comparator function returns True if a is greater or equal to b, and False otherwise.
    """
    return a >= b

def is_sorted(a_list, comparator=increasing_comparator):
    for i in range(0,(len(a_list)-1)):
        if comparator(a_list[i], a_list[i+1]):
            continue
        else:
            return False
    return True

def main():
    list1 = [20,10,30]
    list2 = [30,20,10]
    print(is_sorted(list1))
    print(is_sorted(list1, decreasing_comparator))
    print(is_sorted(list2, increasing_comparator))
    print(is_sorted(list2, decreasing_comparator))

if __name__ == "__main__":
    main()