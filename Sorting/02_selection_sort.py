# +++++++++++ Selection Sort +++++++++++++++++++++
def selection_sort(arr, length):
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if arr[min_index] > arr[j]:
                arr[j], arr[min_index] = arr[min_index], arr[j]


arr = [2, 5, 10, 0, 1, 50, -5]
length = len(arr)  # 7
selection_sort(
    arr=arr,
    length=length,
)
print(f"Sorted array is {arr}")
