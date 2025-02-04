import json

# fdict=f.read().split("\n")[0:-1]
#
# actual_list={}
# for dict in fdict:
#     key=dict.split(":")[0]
#     print(key)
#     list_val=dict.split(":")[1]
#     js=json.loads(list_val)
#     actual_list[key]=js
# print(actual_list)
import sys
arr_of_arr=[[["AP890101-0001", 13, [2]], ["AP890101-0001", 9, [2]]],
    [["AP890101-0001", 14, [3]], ["AP890101-0003", 11, [3]], ["AP890103-0194", 10, [437]], ["AP890103-0191", 8, [437]], ["AP890103-0193", 2, [437]]],
            [["AP890104-0217", 6, [403]],["AP890104-0218", 5, [403]]]]






s=sys.getsizeof('[["AP890101-0001", 1, [2]], ["AP890101-0001", 1, [2]]]')
print(s)

import heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
maxheap= heapq._heapify_max(listForTree)        # for a maxheap!!
print(listForTree)
print(heapq._heappop_max(listForTree))
print(listForTree)
heapq._heappop_max(listForTree)
print(listForTree)
heapq._heappop_max(listForTree)
print(listForTree)
heapq._heappop_max(listForTree)
print(listForTree)
heapq._heappop_max(listForTree)
print(listForTree)
heapq._heappop_max(listForTree)
print(listForTree)

