import heapq


def merge_k_arrays(arr_of_arr):
    # arr_of_arr = [[13, 9, 7, 3],
    #               [14, 11, 10, 8, 2],
    #               [15, 12, 1],
    #               [6, 5, 4]]
    # arr_of_arr=[[[13,"AP890101-0001", [2]], [9,"AP890101-0001",  [2]]],
    # [[14,"AP890101-0001",  [3]], [11,"AP890101-0003",  [3]], [10,"AP890103-0194",  [437]], [8,"AP890103-0191",  [437]], [2,"AP890103-0193",  [437]]],
    #         [[6,"AP890104-0217",  [403]],[5,"AP890104-0218",  [403]]]]
    output_arr = []
    initial_heap = []
    for i in range(0, len(arr_of_arr)):
        initial_heap.append((arr_of_arr[i][0], i, 0))
    heapq._heapify_max(initial_heap)

    while len(initial_heap) != 0:
        max_element = initial_heap[0]
        from_array_index = max_element[1]
        index_in_that_array = max_element[2]
        output_arr.append(max_element[0])

        if index_in_that_array + 1 < len(arr_of_arr[from_array_index]):
            next_item = (
            arr_of_arr[from_array_index][index_in_that_array + 1], from_array_index, index_in_that_array + 1)
            heapq._heapreplace_max(initial_heap, next_item)
        else:
            heapq._heappop_max(initial_heap)
    return output_arr