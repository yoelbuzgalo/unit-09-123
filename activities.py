import arrays
import timing
import re

def unique_array(an_array, value):
    for index in range(len(an_array)):
        if an_array[index] == value:
            return
        elif an_array[index] == None:
            an_array[index] = value
            return

def fill_array(length):
    arr = arrays.Array(length, None)
    for i in range(length):
        unique_array(arr, i)
    return arr

def unique_list(a_list, value):
    for index in range(len(a_list)):
        if a_list[index] == value:
            return
    a_list.append(value)

def fill_list(length):
    a_list = []
    for i in range(length):
        unique_list(a_list, i)
    return a_list

def unique_set(a_set, value):
    if value not in a_set:
        a_set.add(value)
    return

def fill_set(length):
    a_set = set()
    for i in range(0, length-1):
        unique_set(a_set, i)
    return a_set

def sets():
    a_set = {111,3,57, 100}
    print(a_set)
    a_set.add(50000)
    print(a_set)

    b_set = set("foo")
    print(b_set)

def unique_words(filename):
    unique_words = set()
    with open(filename) as file:
        for line in file:
            words = re.findall("[A-Za-z-']+", line)
            for word in words:
                unique_words.add(word.lower())
    return unique_words

def intersection(a_set, b_set):
    intersections = set()
    for keyword in a_set:
        if keyword in b_set:
            intersections.add(keyword)
    return intersections

def main():
    # print(len(unique_words("data/alice.txt")))
    # an_array = timing.time_function(fill_array, 5000)
    # a_list = timing.time_function(fill_list, 5000)
    # print(an_array)
    # print(a_list)
    # sets()
    # a_set = timing.time_function(fill_set, 5000)
    # print(a_set)
    print(intersection({1,2,3}, {2,3,4}))

if __name__ == "__main__":
    main()