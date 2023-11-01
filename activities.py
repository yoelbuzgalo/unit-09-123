import arrays
import timing

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

def main():
    an_array = timing.time_function(fill_array, 5000)
    a_list = timing.time_function(fill_list, 5000)
    print(an_array)
    print(a_list)

if __name__ == "__main__":
    main()