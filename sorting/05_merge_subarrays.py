def merge_subarrays(arr, low, med, high):
    array1 = arr[low : med + 1]
    len1 = len(array1)
    array2 = arr[med + 1 : high]
    len2 = len(array2)
    i = j = 0
    k=low
    while i < len1 and j < len2:
        if array1[i] < array2[j]:
            arr[k]=array1[i]
            i += 1
            k+=1
        elif array2[j] < array1[i]:
            arr[k]=array2[j]
            j += 1
            k+=1
        else:
            arr[k]=array1[i]
            i += 1
            j += 1
            k+=1
    # for adding the remaining elements in new_array
    while i < len1:
        arr[k]=array1[i]
        i += 1
        k+=1
    # for adding the remaining elements in new_array
    while j < len2:
        arr[k]=array2[j]
        j += 1
        k+=1

arr = [10, 15, 20, -1,8, 11, 55]
low = 0
med = 2
high = len(arr)
merge_subarrays(arr=arr, low=low, med=med, high=high)
print(f"Merged sorted array is: {arr}")
