from typing import List
from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from merge import merge_sort
from utils.ansi_colors import BLUE, GREEN, RED, RESET
from utils.custom_types import Number

arr: List[Number] = [7, 2, 5, 1, 9]

def show_menu():
    print(f"{GREEN}Escolha o algoritmo desejado! Array: {arr}{RESET}")
    print(f"{BLUE}1 - Bubble Sort{RESET}")
    print(f"{BLUE}2 - Selection Sort{RESET}")
    print(f"{BLUE}3 - Insertion Sort{RESET}")
    print(f"{BLUE}4 - Merge Sort{RESET}")

    num = int(input("Digite a opção desejada: "))

    res: None | List[Number] = None
    match num:
        case 1:
            res = bubble_sort(arr)
        case 2:
            res = selection_sort(arr)
        case 3:
            res = insertion_sort(arr)
        case 4:
            res = merge_sort(arr)
        case _:
            print(f"{RED}Opção inválida{RESET}")
            exit(0)

    print(f"{GREEN}{res}{RESET}")

if __name__ == "__main__":
    show_menu()
