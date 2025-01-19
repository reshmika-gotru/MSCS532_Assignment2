# Python program for implementation of MergeSort

# Merges two subarrays of array[]
# First subarray is array[l..m]
# Second subarray is array[m+1..r]

def merge(array, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = array[l + i]

	for j in range(0, n2):
		R[j] = array[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			array[k] = L[i]
			i += 1
		else:
			array[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there are any
	while i < n1:
		array[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there are any
	while j < n2:
		array[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the sub-array of arr to be sorted

def mergeSort(array, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(array, l, m)
		mergeSort(array, m+1, r)
		merge(array, l, m, r)

# Sample code to test above
array = [12, 11, 13, 5, 6, 7, 0, 250, -500, 58.5,0.00028,0.0000089]
n = len(array)
print("Given array is")
for i in range(n):
	print("%d" % array[i],end=" ")

mergeSort(array, 0, n-1)
print("\n\n Sorted array is")
for i in range(n):
	print("%d" % array[i],end=" ")
print("\n\n")
