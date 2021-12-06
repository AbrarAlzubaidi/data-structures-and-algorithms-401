def insertion_sort(arr=[]):
    """
    to sort array in an Ascending order after its created
    """
    i=1
    if arr == []:
        raise Exception('empty array')
    while i < len(arr):
        j= i-1
        temp = arr[i]
        if type(arr[i]) == str or type(arr[i]) == bool :
            raise Exception(f'different datatype: string or boolean is exist in position {i}')
        while j>=0 and temp <arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] =temp
        i+=1
    return arr


print(insertion_sort([8,4,23,42,16,15]))



"""
Selection Sort is a sorting algorithm that traverses the array multiple times
as it slowly builds out the sorting sequence.
The traversal keeps track of the minimum value and places it in the front of the array 
which should be incrementally sorted.

SelectionSort(int[] arr)
    DECLARE n <-- arr.Length;
    FOR i = 0; i to n - 1  
        DECLARE min <-- i;
        FOR j = i + 1 to n
            if (arr[j] < arr[min])
                min <-- j;

        DECLARE temp <-- arr[min];
        arr[min] <-- arr[i];
        arr[i] <-- temp;
"""