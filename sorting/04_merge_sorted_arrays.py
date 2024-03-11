def merge(array1, array2):
    len1 = len(array1)
    len2 = len(array2)
    new_array = []  # empty array for adding the elements
    i = j = 0  # tracking the current index of two arrays
    while i < len1 and j < len2:
        if array1[i] < array2[j]:
            new_array.append(array1[i])
            i += 1
        elif array2[j] < array1[i]:
            new_array.append(array2[j])
            j += 1
        else:
            new_array.append(array1[i])
            i += 1
            j += 1
    # for adding the remaining elements in new_array
    while i < len1:
        new_array.append(array1[i])
        i += 1
    # for adding the remaining elements in new_array
    while j < len2:
        new_array.append(array2[j])
        j += 1
    return new_array


array1 = [1, 4, 7]
array2 = [2, 3, 6, 10]
new_array = merge(array1=array1, array2=array2)
print(f"Two sorted arrays after merge is: {new_array}")
