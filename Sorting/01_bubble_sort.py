# ++++++++++++++ Bubble Sort ++++++++++++++++++++++
def bubble_sort(arr, length):
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                # bubbling the bigger element
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


arr = [2, 5, 10, 0, 1, 50, -5]
length = len(arr)  # length:7
bubble_sort(arr=arr, length=length)
print(f"Sorted array is: {arr}")    


