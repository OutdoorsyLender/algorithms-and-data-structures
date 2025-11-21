import time
import random

# Bubble Sort Implementation 
def bubble_sort(numbers):
    list_length = len(numbers)
    for i in range(list_length):
        made_swap = False
        for j in range(0, list_length - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                made_swap = True
        if not made_swap:
            break
    return numbers

# Optimized Bubble Sort
def optimized_bubble_sort(numbers):
    list_length = len(numbers)
    is_sorted = True  # Assume array is sorted initially
    until = list_length - 1
    while until > 0:
        last_swap = 0
        for j in range(until):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                is_sorted = False
                last_swap = j
        if is_sorted:
            break
        until = last_swap
    return numbers

# Merge Sort Implementation
def merge(first_half, second_half):
    first_pos = 0
    second_pos = 0
    result = []
    
    while first_pos < len(first_half) and second_pos < len(second_half):
        if first_half[first_pos] > second_half[second_pos]:
            result.append(second_half[second_pos])
            second_pos += 1
        else:
            result.append(first_half[first_pos])
            first_pos += 1
            
    # Add remaining elements from first half
    result.extend(first_half[first_pos:])
    # Add remaining elements from second half
    result.extend(second_half[second_pos:])
    
    return result

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
        
    middle = len(numbers) // 2
    first_half = merge_sort(numbers[:middle])
    second_half = merge_sort(numbers[middle:])
    
    return merge(first_half, second_half)

# Optimized Merge Sort
def optimized_merge_sort(numbers):
    # Use insertion sort for small arrays
    def insertion_sort(arr, start, end):
        for i in range(start + 1, end + 1):
            key = arr[i]
            j = i - 1
            while j >= start and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def merge_optimized(arr, temp, left, mid, right):
        # Skip if already sorted
        if arr[mid - 1] <= arr[mid]:
            return

        i, j, k = left, mid, left
        while i < mid and j < right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
            
        while i < mid:
            temp[k] = arr[i]
            i += 1
            k += 1
            
        # Copy back
        for i in range(left, k):
            arr[i] = temp[i]

    def merge_sort_internal(arr, temp, left, right):
        if right - left <= 10:  # Use insertion sort for small arrays
            insertion_sort(arr, left, right - 1)
            return
            
        if left < right:
            mid = (left + right) // 2
            merge_sort_internal(arr, temp, left, mid)
            merge_sort_internal(arr, temp, mid, right)
            merge_optimized(arr, temp, left, mid, right)

    numbers = numbers.copy()
    temp = [0] * len(numbers)
    merge_sort_internal(numbers, temp, 0, len(numbers))
    return numbers

# Quick Sort Implementation
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    middle_number = numbers[len(numbers) // 2]
    smaller_numbers = [x for x in numbers if x < middle_number]
    equal_numbers = [x for x in numbers if x == middle_number]
    bigger_numbers = [x for x in numbers if x > middle_number]
    
    return quick_sort(smaller_numbers) + equal_numbers + quick_sort(bigger_numbers)

# Optimized Quick Sort
def optimized_quick_sort(numbers):
    def partition(arr, low, high):
        # Choose median of three as pivot
        mid = (low + high) // 2
        pivot = sorted([
            (arr[low], low),
            (arr[mid], mid),
            (arr[high], high)
        ], key=lambda x: x[0])[1][1]
        arr[pivot], arr[high] = arr[high], arr[pivot]
        
        pivot_value = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot_value:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_internal(arr, low, high):
        while low < high:
            # Use insertion sort for small subarrays
            if high - low < 10:
                insertion_sort = lambda a, l, h: sorted(a[l:h+1])
                arr[low:high+1] = insertion_sort(arr, low, high)
                break
            
            pivot = partition(arr, low, high)
            
            # Recursively sort the smaller partition
            if pivot - low < high - pivot:
                quick_sort_internal(arr, low, pivot - 1)
                low = pivot + 1
            else:
                quick_sort_internal(arr, pivot + 1, high)
                high = pivot - 1

    numbers = numbers.copy()
    quick_sort_internal(numbers, 0, len(numbers) - 1)
    return numbers

# Test Data Generation Functions
def create_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]

def create_reverse_list(size):
    return list(range(size, 0, -1))

def create_almost_sorted_list(size):
    arr = list(range(size))
    swaps = size // 20
    for _ in range(swaps):
        i = random.randint(0, size-2)
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# Testing Functions
def test_sorting_speed(sort_function, numbers, runs=3):
    times = []
    for _ in range(runs):
        start_time = time.perf_counter()  
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return sum(times) / len(times)  # Average time

def run_tests():
    test_sizes = [100, 1000, 10000]
    sorting_methods = {
        'Bubble Sort': bubble_sort,
        'Optimized Bubble Sort': optimized_bubble_sort,
        'Merge Sort': merge_sort,
        'Optimized Merge Sort': optimized_merge_sort,
        'Quick Sort': quick_sort,
        'Optimized Quick Sort': optimized_quick_sort
    }

    for size in test_sizes:
        print(f"\nTesting with list size: {size}")
        print("-" * 50)
        
        # Generate test data
        random_numbers = create_random_list(size)
        reverse_numbers = create_reverse_list(size)
        almost_sorted = create_almost_sorted_list(size)
        
        test_types = {
            'Random': random_numbers,
            'Reverse Sorted': reverse_numbers,
            'Almost Sorted': almost_sorted
        }
        
        for test_name, test_numbers in test_types.items():
            print(f"\nTest case: {test_name}")
            print("-" * 30)
            
            # Get all times first
            times = {}
            for method_name, sort_method in sorting_methods.items():
                times[method_name] = test_sorting_speed(sort_method, test_numbers)
            
            # Find fastest time and check if times are too small 
            fastest_time = min(times.values())
            TIME_THRESHOLD = 0.000001  # 0.1 milliseconds threshold
            
            print("\nResults:")
            print("-" * 30)
            
            if fastest_time < TIME_THRESHOLD:
                print("Time threshold not met")
                print("-" * 30)
            
            # Print results ordered by speed
            for method_name, time_taken in sorted(times.items(), key=lambda x: x[1]):
                if fastest_time < TIME_THRESHOLD:
                    print(f"{method_name}: {time_taken:.6f} seconds (too fast for reliable ratio)")
                else:
                    ratio = time_taken / fastest_time
                    print(f"{method_name}: {time_taken:.6f} seconds (ratio to fastest: {ratio:.2f}x)")

if __name__ == "__main__":
    print("Starting sorting algorithm comparison tests...")
    run_tests()