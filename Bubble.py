import timeit

class Bubble:
    @staticmethod
    def print_array(arr):
        for element in arr:
            print(element, end=" ")

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    a = [35, 10, 31, 11, 26]
    b1 = Bubble()

    print("Before sorting array elements are - ")
    b1.print_array(a)
    
    time_bubble_sort = timeit.timeit(lambda: b1.bubble_sort(a.copy()), number=1)
    
    print("\nAfter sorting array elements are - ")
    b1.print_array(a)
    print("\nExecution Time of Bubble Sort: {:.6f} seconds".format(time_bubble_sort))
    
    a = [35, 10, 31, 11, 26]
    
    time_python_sort = timeit.timeit(lambda: sorted(a), number=1)
    
    print("Execution time for Sort() Function in Python: {:.6f} seconds".format(time_python_sort))
