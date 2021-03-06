"""
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)
"""
def merge_sort(arr):
    """
    to divide array into 2 arrays
    """
    n = len(arr)
    if n>1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    """
    merge arrays together after sort it
    """
    i=0
    j=0
    k=0
    while i<len(left) and j< len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k]= right[j]
            j+=1
        k+=1
    
    while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
  
    while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

print(merge_sort([8,4,23,42,16,15]))
"""
ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
"""