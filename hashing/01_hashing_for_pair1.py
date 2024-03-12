'''
You are given an array of distinct integers and a sum. Check if there's a pair with the given sum in the array.
'''

def sumExists(arr, N, sum):
    isFound=0
    new_set=set() #empty set
    for i in range(N):
        compliment=sum-arr[i]
        if compliment in new_set:
            isFound=1
        else:
            new_set.add(arr[i])
    return isFound
N = 10
arr= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
sum = 14
print(sumExists(arr,N,sum))