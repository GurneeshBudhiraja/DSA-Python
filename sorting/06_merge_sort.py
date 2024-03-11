def merge_subarrays(arr, low, med, high):
    arr1 = arr[low : med + 1]
    arr2 = arr[med + 1 : high + 1]
    len1, len2 = len(arr1), len(arr2)
    i = j = k = 0

    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            arr[low + k] = arr1[i]
            i += 1
        else:
            arr[low + k] = arr2[j]
            j += 1
        k += 1

    # Add any remaining elements
    while i < len1:
        arr[low + k] = arr1[i]
        i += 1
        k += 1
    while j < len2:
        arr[low + k] = arr2[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge_subarrays(arr, low, mid, high)


arr = [-2, 10, 15, 20, -1, 8, 11, 55, 11]
merge_sort(arr, 0, len(arr) - 1)
print(f"Sorted array is: {arr}")
