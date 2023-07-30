def selection_sort(int_list):
    count = 0
    while count < len(int_list)-1:
        lowest = int_list[count]
        lowest_ix = count
        print(f"lowest at the beginning of pass = {lowest}; pass = {count};")
        for ix, i in enumerate(int_list[count+1:]):
            if i < lowest:
                lowest = i
                lowest_ix = ix + count + 1
        print(f"lowest = {lowest}")
        print(f"lowest_ix = {lowest_ix}")
        int_list.insert(count, int_list.pop(lowest_ix))
        print(f"list after the pass end = {int_list}")
        count += 1
    return int_list

print(selection_sort([12, 11, 13, 5, 6]))