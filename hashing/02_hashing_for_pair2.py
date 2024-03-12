'''
You are given an array of integers and an integer sum. You need to find if two numbers in the array exists that have sum equal to the given sum.
'''
def sumExists(arr, N, sum):
    ##Your code here
    isFound=0 
    new_set=set()
    for i in range(N):
        compliment=sum-arr[i]
        if(compliment in new_set):
            isFound=1
            break
        else:
            new_set.add(arr[i])
    return isFound
N = 4
arr = [4,3,5,6]
sum = 7
print(sumExists(arr,N,sum))
