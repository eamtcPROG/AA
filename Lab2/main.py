import random
import time
import matplotlib.pyplot as plt

def generate_random_array(n, lower, upper):
    arr = [random.randint(lower, upper) for _ in range(n)]
    return arr

def quick_sort(array_for_quick_sort):
    if len(array_for_quick_sort) <= 1:
        return array_for_quick_sort

    pivot = array_for_quick_sort[len(array_for_quick_sort) // 2]
    left = [x for x in array_for_quick_sort if x < pivot]
    middle = [x for x in array_for_quick_sort if x == pivot]
    right = [x for x in array_for_quick_sort if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(array_for_merge_sort):
    if len(array_for_merge_sort) <= 1:
        return array_for_merge_sort

    # Split the array into two halves
    mid = len(array_for_merge_sort) // 2
    left = array_for_merge_sort[:mid]
    right = array_for_merge_sort[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the sorted halves
    i = j = 0
    merged = []
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1

    merged += left_sorted[i:]
    merged += right_sorted[j:]

    return merged

def heap_sort(array_for_heap_sort):
    # Build a max heap from the input array
    array_for_heap_sort = build_max_heap(array_for_heap_sort)

    # Perform the sort by repeatedly extracting the maximum element
    sorted_arr = []
    for i in range(len(array_for_heap_sort)):
        sorted_arr.append(array_for_heap_sort[0])
        array_for_heap_sort[0] = array_for_heap_sort[-1]
        array_for_heap_sort.pop()
        array_for_heap_sort = max_heapify(array_for_heap_sort, 0)

    return sorted_arr

def build_max_heap(array):
    for i in range(len(array) // 2, -1, -1):
        array = max_heapify(array, i)
    return array

def max_heapify(array_heapify, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < len(array_heapify) and array_heapify[left] > array_heapify[largest]:
        largest = left

    if right < len(array_heapify) and array_heapify[right] > array_heapify[largest]:
        largest = right

    if largest != i:
        array_heapify[i], array_heapify[largest] = array_heapify[largest], array_heapify[i]
        array_heapify = max_heapify(array_heapify, largest)
    return array_heapify

def bubble_sort(array_bubble_sort):
    n = len(array_bubble_sort)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array_bubble_sort[j] > array_bubble_sort[j + 1]:
                temp = array_bubble_sort[j]
                array_bubble_sort[j] = array_bubble_sort[j + 1]
                array_bubble_sort[j + 1] = temp

    return array_bubble_sort

def time_execution(algorithm, arr):
    start = time.time()
    algorithm(arr)
    end = time.time()
    return end - start

def print_for_plot():
    plt.xlabel('Input size')
    plt.ylabel('Execution time (seconds)')
    plt.legend()
    plt.show()

def plot_results(n_values, time_values,title,label):
    plt.plot(n_values, time_values, label=label)
    plt.title(title)
    print_for_plot()

def plot_all_results(n_values, time_values_quick, time_values_merge, time_values_heap, time_values_bubble):
    plt.plot(n_values, time_values_quick, label='Quick sort')
    plt.plot(n_values, time_values_merge, label='Merge sort')
    plt.plot(n_values, time_values_heap, label='Heap sort')
    plt.plot(n_values, time_values_bubble, label='Bubble sort')
    print_for_plot()

def plot_qs_ms_hs(n_values, time_values_quick, time_values_merge, time_values_heap):
    plt.plot(n_values, time_values_quick, label='Quick sort')
    plt.plot(n_values, time_values_merge, label='Merge sort')
    plt.plot(n_values, time_values_heap, label='Heap sort')
    print_for_plot()

def print_array(arr):
    print("[", end="")
    for i in range(len(arr)):
        if i != len(arr) - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i], end="")
    print("]")

if __name__ == '__main__':
    # Set up variables for testing
    n_values = [100, 1000, 2500]
    lower = 0
    upper = 100000

    # Generate random arrays for testing
    arrays = [generate_random_array(n, lower, upper) for n in n_values]

    unsorted_arr_for_q = arrays
    unsorted_arr_for_m = arrays
    unsorted_arr_for_h = arrays
    unsorted_arr_for_b = arrays

    # Test each algorithm on each array and record execution time
    quick_sort_times = []
    merge_sort_times = []
    heap_sort_times = []
    bubble_sort_times = []

    for arr in unsorted_arr_for_b:
        bubble_sort_times.append(time_execution(bubble_sort, arr.copy()))

    for arr in unsorted_arr_for_q:
        quick_sort_times.append(time_execution(quick_sort, arr.copy()))

    for arr in unsorted_arr_for_m:
        merge_sort_times.append(time_execution(merge_sort, arr.copy()))

    for arr in unsorted_arr_for_h:
        heap_sort_times.append(time_execution(heap_sort, arr.copy()))

    # Plot the results
    plot_results(n_values, quick_sort_times, 'Quick sort','Quick sort')
    plot_results(n_values, merge_sort_times, 'Merge sort', 'Merge sort')
    plot_results(n_values, heap_sort_times, 'Heap sort', 'Heap sort')
    plot_results(n_values, bubble_sort_times, 'Bubble sort', 'Bubble sort')

    plot_all_results(n_values, quick_sort_times, merge_sort_times, heap_sort_times, bubble_sort_times)

    n_values = [10000, 100000, 1000000]
    lower = 0
    upper = 1000000

    arrays = [generate_random_array(n, lower, upper) for n in n_values]

    unsorted_arr_for_q = arrays
    unsorted_arr_for_m = arrays
    unsorted_arr_for_h = arrays

    quick_sort_times = []
    merge_sort_times = []
    heap_sort_times = []

    for arr in unsorted_arr_for_q:
        quick_sort_times.append(time_execution(quick_sort, arr.copy()))

    for arr in unsorted_arr_for_m:
        merge_sort_times.append(time_execution(merge_sort, arr.copy()))

    for arr in unsorted_arr_for_h:
        heap_sort_times.append(time_execution(heap_sort, arr.copy()))

    plot_qs_ms_hs(n_values, quick_sort_times, merge_sort_times, heap_sort_times)