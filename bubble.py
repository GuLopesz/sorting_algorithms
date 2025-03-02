from typing import List

from utils.custom_types import Number

def bubble_sort(arr: List[Number]) -> List[Number]:
    x = len(arr)
    for i in range (x):
        for j in range(0, x-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
