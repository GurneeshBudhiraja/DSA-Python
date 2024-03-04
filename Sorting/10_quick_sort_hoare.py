# ++++++++++ Quicksort using Hoare's partition scheme ++++++++++++++++++
def hoarePartiton(arr,low,high):
    pivot=arr[low]
    i=low-1
    j=high+1
    while True:
        i+=1
        while(arr[i]<pivot):
            i+=1
        j-=1
        while(arr[j]>pivot):
            j-=1
        if(i>=j):
            return j
        arr[i],arr[j]=arr[j],arr[i]

def quickSort(arr,low,high):
    if(low<high):
        partitionIndex=hoarePartiton(arr=arr,low=low,high=high)
        quickSort(arr=arr,low=low,high=partitionIndex)
        quickSort(arr=arr,low=partitionIndex+1,high=high)



arr = [0,7, 1, 4, 100, 2, 5, 3, 4]
low=0
high=len(arr)-1
quickSort(arr=arr,low=low,high=high)
print(f"Sorted array is {arr}")

