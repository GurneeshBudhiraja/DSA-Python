'''
Given an array arr[] of size n, find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.
'''
from collections import Counter
def firstRepeating(arr,n):
    ans=-1
    new_dict=Counter(arr)
    for (index,value) in enumerate(arr):
        if(value in new_dict and new_dict[value]>1):
            ans=index
            return ans+1
        else:
            continue
    return ans

n = 7
arr = [1 ,5 ,3 ,4 ,3 ,5 ,6]

print(firstRepeating(arr,n))