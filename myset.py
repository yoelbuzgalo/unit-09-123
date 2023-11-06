def make_myset(length, hash_func=hash):
    table = [[] for _ in range(length)]
    return (hash_func, table)

def add(myset, element):
    hash_func, table = myset
    length = len(table)
    hash_code = hash_func(element)
    index = hash_code % len(table)
    # check if already exists
    if element not in table[index]:
        table[index].append(element)


def main():
    a_set = make_myset(7)
    print(a_set)
    add(a_set, "One")
    print(a_set)
    add(a_set, "Two")
    print(a_set)
    add(a_set, "Three")
    print(a_set)

main()