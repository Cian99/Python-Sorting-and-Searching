#Q1
def bubble_sort():
    #array used in Q1
    array = [15, 18, 2, 19, 18, 20, 34, 109, 2]
    print("Sorting using Bubble Sort:")
    #variable for the length of the array
    n = len(array)

    #goes through all the array elements
    for i in range(n):
        for j in range(0, n-i-1):
            #traverse the array from - to n-i-1
            #swap if element found is greater than the next one
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                #shows the result step by step as the program is executed
                print("Step by step: ", array)
    #prints final result
    print("Sorted array is: ", array)


def insertion_sort():
    #array used in Q1
    array = [15, 18, 2, 19, 18, 20, 34, 109, 2]
    print("\nSorting using Insertion Sort:")
    #variable for the length of the array
    n = len(array)

    #goes from 1 to the length of the array
    for i in range(1, n):
        #covers from the item to the left of i and works left
        j = i-1
        #if item on right is less than item on left they swap places
        while array[j] > array[j+1] and j >= 0:
            array[j], array[j+1] = array[j+1], array[j]
            j -=1
            #shows the result step by step as the program is executed
            print("Step by step: ", array)
    #prints final result
    print("Sorted array is: ", array)


def selection_sort():
    #array used in Q1
    array = [15, 18, 2, 19, 18, 20, 34, 109, 2]
    print("\nSorting using Selection Sort:")
    #variable for the length of the array
    n = len(array)
    
    #outer loop goes from 0 to second last item in list
    for i in range (0, n-1):
        #initial location for minimum item in the list 
        minIndex = i

        #inner loop sorts the list
        for j in range(i+1, n):

            #if number at j is less than current min then j is the
            #new location for the minimum number
            if array[j] < array[minIndex]:
                minIndex = j
                
        if minIndex != i:
            array[i], array[minIndex] = array[minIndex], array[i]
        #shows the result step by step as the program is executed
        print("Step by step: ", array)
    #prints final result
    print("Sorted array is: ", array)
    
def main():
    bubble_sort()
    insertion_sort()
    selection_sort()

main()
