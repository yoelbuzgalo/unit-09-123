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

def names():
    people = {}
    people["YBB"] = "Yoel Baer Buzgalo"
    people["UAB"] = "Uzi Alden Buzgalo"
    people["AMB"] = "Anne Marie Alden Buzgalo"
    print(people)

def print_dict(dict):
    for key in dict:
        value = dict[key]
        print("Key:", key, "Value:", value)

def count_words(filename):
    words_count = {}
    with open(filename) as file:
        for line in file:
            words = re.findall("[A-Za-z-']+", line)
            for word in words:
                word.lower()
                if word not in words_count:
                    words_count[word] = 0
                words_count[word] += 1
    return words_count

words = count_words("data/alice.txt")

def sort_key(word):
    return words[word]

def main():
    sorted_words = sorted(words, key=sort_key)
    tuples = []
    for key in words:
        tuples.append((words[key], key))
    sorted_words = sorted(tuples, reverse=True)
    for word in sorted_words[:20]:
        print(word[1])
    # print(len(unique_words("data/alice.txt")))
    # an_array = timing.time_function(fill_array, 5000)
    # a_list = timing.time_function(fill_list, 5000)
    # print(an_array)
    # print(a_list)
    # sets()
    # a_set = timing.time_function(fill_set, 5000)
    # print(a_set)
    #print(intersection({1,2,3}, {2,3,4}))
    # some_dict = {"first": 1,
    #              "another": 2
    #              }
    # print_dict(some_dict)

if __name__ == "__main__":
    main()