

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self, capacity):
        # We need to know: 1. place to hold stuff 2. capacity 3. how much of capacity we're using to indicate out of bounds errors
        self.capacity = capacity
        self.count = 0
        self.elements = [None] * capacity  # representative data structure


# Double the size of the given array
def resize_array(array):
    # We need the current size, capacity,and all elements, so pass in the array
    new_capacity = array.capacity * 2
    new_elements = [None] * new_capacity

    # Copy over all prev elements
    for i in range(array.count):
        new_elements[i] = array.elements[i]

    # Reset array attrs to new attrs
    array.capacity = new_capacity
    array.elements = new_elements


# Return an element of a given array at a given index -> so we need an array and index
def array_read(array, index):
    # Throw an error if array is out of the current count
    # Your code here
    if index >= array.count:
        print(f"Error, element {index} is out of bounds.")

    return array.elements[index]


# Insert an element in a given array at a given index -> so we need an array, element, index
def array_insert(array, element, index):
    # Throw an error if array is out of the current count... capacity??
    if index >= array.capacity:
        # print(f"Error, element {index} is out of bounds.")
        print("Error, array is too small, increasing size.")

    # Resize the array if the number of elements is over capacity
    if array.count == array.capacity:  # call resize_array method
        resize_array(array)

    # Move the elements to create a space at 'index'
    # Think about where to start!
    # backwards for loop -- range(start, stop, step)
    for i in range(array.count, index, -1):
        array.elements[i] == array.elements[i-1]

    # Add the new element to the array and update the count
    array.elements[index] = element
    array.count += 1


# Add an element to the end of the given array
def array_append(array, element):

    # Hint, this can be done with one line of code
    # (Without using a built in function)

    # Your code here
    array_insert(array, element, array.count)


# Remove the first occurence of the given element from the array -> need array, element
# Throw an error if the value is not found
def array_remove(array, element):
    # Your code here
    removed = False
    current = 0
    while not removed:  # removed is False
        # check if current is outside of array
        if current >= array.count:
            print("Error, value not found.")
            break

        if array.elements[current] == element:
            # found element, so removed = True
            removed = True

            # shift all elements after the counter index up by 1
            for i in range(current, array.count):
                array.elements[i] == array.elements[i+1]

            # decrement the array count
            array.count -= 1

        else:
            current += 1


# Remove the element in a given position and return it -> need array, index
# Then shift every element after that occurrance to fill the gap
def array_pop(array, index):
    # Throw an error if array is out of the current count
    # Your code here
    # Improvement TODO: build helper function to handle this repetitive error
    # Have the helper check for above and below bounds

    if index >= array.count or index < 0:
        print(f"Error, element {index} is out of bounds.")
        return None

    # find value in index and store it to return it
    return_value = array.elements[index]

    # TODO: write an array shift function for here and array_remove
    for i in range(index + 1, array.count, 1):
        array.elements[i - 1] = array.elements[i]  # shifts element over

    array.count -= 1
    # because all unused elements/empty slots in array should have None value, so deleting something creates empty slot
    array.elements[array.count] = None

    return return_value


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.count):
        string += str(array.elements[i])
        if i < array.count - 1:
            string += ", "

    string += "]"
    print(string)


# # Testing
arr = array(1)

array_insert(arr, "STRING1", 0)     # [STRING1]
array_print(arr)                    # [STRING1]
print(array_pop(arr, 0))            # should print STRING1
array_print(arr)                    # []
array_insert(arr, "STRING1", 0)     # [STRING1]
array_append(arr, "STRING4")        # [STRING1, STRING4]
array_print(arr)                    # [STRING1, STRING4]
array_insert(arr, "STRING2", 1)     # replaced STRING4 -> [STRING1, STRING2]
array_insert(arr, "STRING3", 2)     # [STRING1, STRING2, STRING3]
array_print(arr)                    # [STRING1, STRING2, STRING3]
