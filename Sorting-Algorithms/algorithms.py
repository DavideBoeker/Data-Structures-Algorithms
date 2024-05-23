import pandas as pd
import numpy as np



def main():

    unsorted_list = [10, 5, 2, 7, 4, 9, 8, 1, 3, 6]
    # sorted_list = quick_sort(unsorted_list)
    # sorted_list = merge_sort(unsorted_list)
    sorted_list = heap_sort(unsorted_list)
    print(sorted_list)



def quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    else:
        pivot = unsorted_list.pop() # Use last element as pivot
        less = [x for x in unsorted_list if x <= pivot]
        greater = [x for x in unsorted_list if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    

def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left_half = unsorted_list[:mid]
        right_half = unsorted_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                unsorted_list[k] = left_half[i]
                i += 1
            else:
                unsorted_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            unsorted_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            unsorted_list[k] = right_half[j]
            j += 1
            k += 1

        return unsorted_list
    


def heap_sort(unsorted_list):
    n = len(unsorted_list)

    for i in range(n//2 - 1, -1, -1):
        heapify(unsorted_list, i, 0)

    for i in range(n-1, 0, -1):
        unsorted_list[i], unsorted_list[0] = unsorted_list[0], unsorted_list[i]
        heapify(unsorted_list, i, 0)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[i], arr[largest]
        heapify(arr, n, largest)
                   





if __name__ == "__main__":
    main()