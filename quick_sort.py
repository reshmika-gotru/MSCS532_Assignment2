# Python program for implementation of QuickSort

# This function takes first element as pivot, places the pivot element at its correct position in sorted array, 
# and places all smaller (smaller than pivot) before it.

def pivot(array, begin, end):
    
 
#initializing 
    pivot = array[begin]
    low = begin + 1
    high = end
 
 
    while True:
   
#moving high towards left
        while low <= high and array[high] >= pivot:
            high = high - 1
 
#moving low towards right 
        while low <= high and array[low] <= pivot:
            low = low + 1
 
#verifying if low and high have crossed
        if low <= high:
 
#swapping values to rearrange
            array[low], array[high] = array[high], array[low]
          
        else:
#coming out of the loop if low > high
            break
 
#swapping pivot with high so that pivot is at its right position 
    array[begin], array[high] = array[high], array[begin]
 
#returning pivot position
    return high
 
 
def quick_sort(array, begin, end):
    if begin >= end:
        return
 
#calling pivot 
    p = pivot(array, begin, end)
#recursive call on left half
    quick_sort(array, begin, p-1)
#recursive call on right half
    quick_sort(array, p+1, end)
 
 
array = [5,1,3,9,8,2,7,4,-50,0,0.0095,-47.5]
 
quick_sort(array, 0, len(array) - 1)
print(array)

array = [5,1,3,9,8,2,7,-100,-5,0,4,6,75.9,0.08,-85.7]
 
quick_sort(array, 0, len(array) - 1)
print(array)