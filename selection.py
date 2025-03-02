from typing import List

from utils.custom_types import Number

def selection_sort(arr: List[Number]) -> List[Number]:
    for i in range(len(arr)):
        men = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[men]:
                men = j
        arr[i], arr[men] = arr[men], arr[i]
    
    return arr

