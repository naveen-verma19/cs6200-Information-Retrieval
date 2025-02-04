def delta_encode_arr(arr):
    new_arr = []
    new_arr.append(arr[0])
    for x in range(1, len(arr)):
        new_arr.append(arr[x] - arr[x - 1])

    return new_arr


# inplace
def delta_decode(arr):
    for x in range(1, len(arr)):
        arr[x] = arr[x] + arr[x - 1]


# arr = [432, 456, 498, 39, 105, 223, 314]
# enc = delta_encode_arr(arr)
# print(enc)
#
# delta_decode(enc)
# print(enc)
