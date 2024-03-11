def insertion_sort(arr, length):
    for i in range(1, length):
        j = i - 1
        temp = arr[i]  # storing the variable needs to be compared
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


arr = [2, 5, 10, 0, 1, 50, -5]
length = len(arr)  # 7
insertion_sort(arr=arr, length=length)
print(f"Sorted Array is {arr}")
