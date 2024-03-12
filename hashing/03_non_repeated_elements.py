'''
You are given an array of integers. You need to print the count of non-repeated elements in the array.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
'''

from collections import Counter
def countNonRepeated(arr,n):
    new_dict=Counter(arr)
    count=len([key for key,value in new_dict.items() if value==1])
    return count    
    

arr = [4,3,5,6]
n=4
print(countNonRepeated(arr,n))