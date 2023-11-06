import arrays
import timing
import re
import random

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
    if value in a_set: 
        return
    a_set.add(value)

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

def collisions(filename, length, hash_func=hash):
    an_array = arrays.Array(length, None)
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if len(line) != 0:
                hash_code = hash(line)
                if an_array[hash_code % len(an_array)] == None:
                    an_array[hash_code % len(an_array)] = line
                    count += 1
                else:
                    return count
    return count

def sort_key(word):
    return words[word]

def hashes():
    print(hash("Hello World!"))
    print(hash("Hello World!"))
    print(hash("Hello World!"))
    print(hash("Hello World!"))
    print(hash("Yoel"))
    print(hash("A"*10000))

def make_myset(length, hash_func=hash):
    table = [[] for _ in range(length)]
    return (hash_func, table)


def main():
    # print(collisions("data/alice.txt", 100))
    # sorted_words = sorted(words, key=sort_key)
    # tuples = []
    # for key in words:
    #     tuples.append((words[key], key))
    # sorted_words = sorted(tuples, reverse=True)
    # for word in sorted_words[:20]:
    #     print(word[1])
    # hashes()
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

    a_set = make_myset(10)
    print(a_set)

if __name__ == "__main__":
    main()