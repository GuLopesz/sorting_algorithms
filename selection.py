def selection_sort(arr):
    for i in range(len(arr)):
        men = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[men]:
                men = j
        arr[i], arr[men] = arr[men], arr[i]
    
    return arr

