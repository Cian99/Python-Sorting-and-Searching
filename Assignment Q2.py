#Q2
def binary_search(array, target):
    #define lower and upper bound
    lower_bound = 0
    upper_bound = len(array)-1
    #this only works while lower bound is less than or equal to upper bound
    while lower_bound <= upper_bound:
        #find mid value
        mid = lower_bound + (upper_bound - lower_bound) // 2
        mid_value = array[mid]
        #if mid is equal to target number then the job is done
        if mid_value == target:
            #displays the position in the human way of counting
            print("Searching for", target,", current number:", array[mid])
            return mid + 1
        #if not then either the upper or lower bound need to change
        # If element is smaller than mid, then it can only be present in left subarray
        elif target < mid_value:
            print("Searching for", target,", current number:", array[mid])
            upper_bound = mid - 1
        # Else the element can only be present in right subarray
        else:
            print("Searching for", target,", current number:", array[mid])
            lower_bound = mid + 1
    # Element is not present in the array
    return None


def linear_search(array, target):
    #i serves as a counter here
    i = 0
    #loop only works when the counter is less than the array length
    while i < len(array):
        #works from one number to the next, checking if it is the target number
        print("Searching for", target,", current number:", array[i])
        position = i + 1
        if array[i] == target:

            #if found it returns the location
            return position
        i = i + 1
    #if not found it says there is none 
    return None

#Binary
#array used in Q2
array = [15, 18, 2, 19, 18, 20, 34, 109, 2]
# however in binary search the array needs to be sorted in order
#we found this in Q1 to be 
array_sorted = [2, 2, 15, 18, 18, 19, 20, 34, 109]
#values searching for
target1 = 34
target2 = 76
#searching for the target numbers
print("Binary Search:")
print("Binary Search for 34: ", binary_search(array_sorted, target1))
print("Binary Search for 76: ", binary_search(array_sorted, target2), "\n")

#Linear
#array used in Q2
array = [15, 18, 2, 19, 18, 20, 34, 109, 2]
#values searching for
target1 = 34
target2 = 76
#searching for the target numbers
print("Linear Search:")
print("Linear Search for 34: ", linear_search(array, target1))
print("Linear Search for 76: ", linear_search(array, target2))
