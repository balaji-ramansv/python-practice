from copy import deepcopy
from xml.dom.minidom import AttributeList


# def min_bribes(q):
#     orig_q = sorted(q)
#     # orig_vs_final = zip(orig_q, q)
#     # displaced = []
#     chunks = []
#     temp = []
#     for i in range(len(q)):
#         if i > 0 and q[i] == q[i-1] + 1:
#             if temp:
#                 temp.append(q[i])
#             else:
#                 temp.extend([q[i-1], q[i]])
#         else:
#             if temp:
#                 chunks.append(temp)
#             temp = []
#     if temp:
#         chunks.append(temp)
#     print(f"temp -- {temp}")
#     print(f"chunks -- {chunks}")
#     print(chunks)

#     remaining = deepcopy(q)
#     for chunk in chunks:
#         for item in chunk:
#             remaining.remove(item)
#     print(f"remaining -- {remaining}")

#     counter = 0
#     bribes = 0
#     processed = []
#     while counter < len(remaining):
#         temp_bribes = 0
#         val = remaining[counter]
#         counter += 1
#         for x in remaining:
#             if val > x and x not in processed:
#                 temp_bribes += 1
#                 print(f"{val} bribes {x}")
#         for chunk in chunks:
#             pursue_further = True
#             for item in chunk:
#                 if val > item and q.index(val) < q.index(item):
#                     temp_bribes += 1
#                     print(f"{val} bribes {item}")
#                 else:
#                     pursue_further = False
#                     break
#             if not pursue_further:
#                 break
#         processed.append(val)
#         bribes += temp_bribes
#         if temp_bribes >= 3:
#             return "Too chaotic"
#     return bribes

def min_bribes(q):
    def return_generator(alist):
        for i in alist:
            yield i

    dup_q = q
    bribes = 0
    for v1 in return_generator(q):
        temp_bribes = 0
        start = False
        for v2 in return_generator(dup_q):
            if v1 != v2 and not start:
                continue
            elif v1 == v2:
                start = True
                continue
            elif v1 > v2:
                temp_bribes += 1
        if temp_bribes >= 3:
            print("Too chaotic")
            return
        bribes += temp_bribes
    print(f"{bribes}")
    
    

#print(min_bribes([2, 5, 1, 3, 4]))
# [1,2,3,5,4] 5 bribes 4
# [1,2,5,3,4] 5 bribes 3
# [2,1,5,3,4] 2 bribes 1
# [2,5,1,3,4] 5 bribes 1

#print(min_bribes([2, 1, 5, 3, 4]))
print(min_bribes([1, 2, 5, 3, 7, 8, 6, 4]))
# 1,2,3,4,5,6,7,8
# 1,2,3,5,4,6,7,8 - 5 bribes 4
# 1,2,5,3,4,6,7,8 - 5 bribes 3
# 1,2,5,3,6,4,7,8 - 6 bribes 4
# 1,2,5,3,6,7,4,8 - 7 bribes 4
# 1,2,5,3,6,7,8,4 - 8 bribes 4
# 1,2,5,3,7,6,8,4 - 7 bribes 6
# 1,2,5,3,7,8,6,4 - 8 bribes 6