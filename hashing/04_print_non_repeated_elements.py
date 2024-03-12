'''
You are given an array of integers. You need to print the non-repeated elements as they appear in the array.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
'''

from collections import OrderedDict
def printNonRepeated(arr,n):
    new_dict=OrderedDict()
    for i in arr:
        if i not in new_dict:
            new_dict[i]=1
        else:
            new_dict[i]+=1
    
    array=[key for key,value in new_dict.items() if value==1]
    return array




n = 10
arr= [1,1,2,2,3,3,4,5,6,7]
print(printNonRepeated(arr,n))