# ++++++++++++++ Quick sort using the lomuto partiton +++++++++++++++++++++
def lomutoPartiton(arr,low,high):
    pivot=arr[high]
    smallestIndex=low-1
    for i in range(low,high+1):
        if(arr[i]<pivot):
            smallestIndex+=1
            arr[smallestIndex],arr[i]=arr[i],arr[smallestIndex]
    arr[smallestIndex+1],arr[high]=pivot,arr[smallestIndex+1]
    return smallestIndex+1


def quickSort(arr,low,high):
    if(low<high):
        pivotIndex=lomutoPartiton(arr,low,high)
        quickSort(arr,low,pivotIndex-1)
        quickSort(arr,pivotIndex+1,high)

arr = [7, 1, 4, 6, 2, 5, 3, 4]
low=0
high=len(arr)-1
quickSort(arr=arr,low=low,high=high)
print(f"Sorted array is {arr}")
