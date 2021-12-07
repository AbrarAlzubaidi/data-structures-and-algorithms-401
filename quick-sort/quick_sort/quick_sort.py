"""
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)
"""
def swap(arr, i, low):
    temp = arr[i]
    arr[i]= arr[low]
    arr[low]= temp


def partition(arr, left, right):
    pivot = arr[right]
    low = left-1
    for i in range(left, right):
        if arr[i]<= pivot:
            low+=1
            swap(arr, i, low)
    swap(arr, right, low+1)
    return low+1
            

def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position-1)
        quick_sort(arr, position+1, right)
    return arr


arr = [8,4,23,42,16,15]
n = len(arr)
print(quick_sort(arr, 0, n-1))
