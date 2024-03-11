# +++++++++++++ Lomuto Partition: pivot is the last element +++++++++++++++++++++++++++++++
def lomutoPartition(arr):
    start = -1  # index of smaller element
    length = len(arr)  # length of array
    pivot = arr[length - 1]  # pivot element (last item of the array)
    for i in range(length):
        if arr[i] < pivot:
            start += 1
            arr[start], arr[i] = arr[i], arr[start]
    arr[start + 1], arr[length - 1] = arr[length - 1], arr[start + 1]
    return start + 1


arr = [7, 1, 4, 6, 2, 5, 3, 4]
pivotIndex = lomutoPartition(arr=arr)
print(f"Sorted array is {arr}")
print(f"The pivot element is at index {pivotIndex}")
