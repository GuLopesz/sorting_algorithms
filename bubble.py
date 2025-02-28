def bubble_sort(arr):
    x = len(arr)
    for i in range (x):
        for j in range(0, x-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
