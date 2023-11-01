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

def main():
    an_array = timing.time_function(fill_array, 5000)
    print(an_array)

if __name__ == "__main__":
    main()