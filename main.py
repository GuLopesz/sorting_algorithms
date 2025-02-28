from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from merge import merge_sort



arr = [7, 2, 5, 1, 9]

def show_menu():
    print("Escolha o algoritmo desejado!")
    print("1 - Bubble Sort")
    print("2 - Selection Sort")
    print("3 - Insertion Sort")
    print("4 - Merge Sort")
    print("5 - Quick Sort")
    print("6 - Radix Sort")
    

    num = int(input("Digite a opção desejada: "))

    if num == 1:
        bubble_sort(arr)
        print(arr)
    elif num == 2:
        selection_sort(arr)
        print(arr)
    elif num == 3:
        insertion_sort(arr)
        print(arr)
    elif num == 4:
        merge_sort(arr)
        print(arr)
    
        
if __name__ == "__main__":
    show_menu()