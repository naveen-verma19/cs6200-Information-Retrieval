import heapq


def merge_k_arrays(arr_of_arr):
    # arr_of_arr = [[13, 9, 7, 3],
    #               [14, 11, 10, 8, 2],
    #               [15, 12, 1],
    #               [6, 5, 4]]

    output_arr = []
    initial_heap = []
    for i in range(0, len(arr_of_arr)):
        # if arr_of_arr[i][0] == 1:  # if first element is 1 then rest all will be one(reverse sorted)
        #     ones_list.extend(arr_of_arr[i])
        # else:
        initial_heap.append((arr_of_arr[i][0], i, 0))
    heapq._heapify_max(initial_heap)

    while len(initial_heap) != 0:
        max_element = initial_heap[0]
        from_array_index = max_element[1]
        index_in_that_array = max_element[2]
        output_arr.append(max_element[0])

        from_array = arr_of_arr[from_array_index]
        next_element_to_be_inserted_index = index_in_that_array + 1
        if next_element_to_be_inserted_index < len(from_array):
            # here if i see 1 in the array i dont push it in the heap
            next_element_to_be_inserted = from_array[next_element_to_be_inserted_index]
            next_item = (
                next_element_to_be_inserted, from_array_index, next_element_to_be_inserted_index)
            heapq._heapreplace_max(initial_heap, next_item)

        else:
            heapq._heappop_max(initial_heap)

    return output_arr

# arr_of_arr=[[[13,"AP890101-0001", [2]], [9,"AP890101-0001",  [2]],[1,"AP890101-0001",  [2]]],
#     [[14,"AP890101-0001",  [3]], [11,"AP890101-0003",  [3]], [10,"AP890103-0194",  [437]], [1,"AP890103-0191",  [437]], [1,"AP890103-0193",  [437]]],
#             [[6,"AP890104-0217",  [403]],[1,"AP890104-0218",  [403]]],
#                 [[1,"AP890104-0219",  [403]],[1,"AP890104-0267",  [403]]]]
# print(merge_k_arrays(arr_of_arr))
