def rotate(arr, k):
    sub_arr = arr[-k:]
    print(sub_arr)
    for i in sub_arr:
        arr.remove(i)
    sub_arr.extend(arr)
    print(sub_arr)

rotate([1,2,3,4,5], 3)