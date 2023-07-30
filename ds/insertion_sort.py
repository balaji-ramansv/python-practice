def insertion_sort(int_list):
    count = 1
    print(f"In the beginning: {int_list}")
    while count < len(int_list):
        key = int_list[count]
        print(f"Pass no = {count}; Key = {key};")
        for ix, i in enumerate(int_list[0:count]):
            if key < i:
                int_list.insert(ix, int_list.pop(count))
                break
        print(int_list, "\n")
        count += 1
        
    return int_list



print(f"Sorted list = {insertion_sort([12, 11, 13, 5, 6])}")