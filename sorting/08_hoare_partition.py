# +++++++ Hoare's partiton +++++++++++++++++
def hoarePartition(arr, l, h):
    pivot = arr[l]  # pivot element (first element of the array)
    i = l - 1  # before the start of the array
    j = h + 1  # after the end of the array
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


arr = [5, 3, 8, 4, 2, 7, 1, 10]
l = 0
h = len(arr) - 1
pivotIndex = hoarePartition(arr, l=l, h=h)
print(f"Sorted array is {arr}")
print(f"Index of the pivot element is {pivotIndex}")
