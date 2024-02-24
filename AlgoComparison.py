import timeit

def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp <= arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp        

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        small = i
        for j in range(i+1, n):
            if arr[j] < arr[small]:
                small = j
        arr[small], arr[i] = arr[i], arr[small]
        
if __name__ == "__main__":
    a = [92, 50, 5, 20, 11, 22]
    
    print("Bubble Sort------------")
    print("Before sorting array elements are - ")
    print(a)
    time_bubble_sort = timeit.timeit(lambda: bubble_sort(a), number=1)
    print("\nAfter sorting array elements are - ")
    print(a)
    print("\nExecution Time of Bubble Sort: {:.6f} seconds".format(time_bubble_sort))
    DefaultSorted=timeit.timeit(lambda: sorted(a),number=1)
    print("\nExecution Time of Sorted() Function in Python: {:.6f} seconds".format(DefaultSorted))
    
    a = [92, 50, 5, 20, 11, 22]
    
    print("Insertion Sort------------")
    print("Before sorting array elements are - ")
    print(a)
    IStime = timeit.timeit(lambda: InsertionSort(a), number=1)
    print("\n\nAfter sorting array elements are - ")
    print(a)
    print("\nExecution Time of Insertion Sort: {:.6f} seconds".format(IStime))
    DefaultSorted=timeit.timeit(lambda: sorted(a),number=1)
    print("\nExecution Time of Sorted() Function in Python: {:.6f} seconds".format(DefaultSorted))
    
    a = [92, 50, 5, 20, 11, 22]
    
    print("Selection Sort------------")
    print("Before sorting array elements are - ")
    print(a)
    time_selection_sort = timeit.timeit(lambda: selection_sort(a), number=1)
    print("\nAfter sorting array elements are - ")
    print(a)
    print("\nExecution Time of Bubble Sort: {:.6f} seconds".format(time_selection_sort))
    DefaultSorted=timeit.timeit(lambda: sorted(a),number=1)
    print("\nExecution Time of Sorted() Function in Python: {:.6f} seconds".format(DefaultSorted))
    

