def rotate(L, d, n):
 k = L.index(d)
 new_lis = []
 new_lis = L[k+1:]+L[0:k+1]
 return new_lis


if __name__ == '__main__':
	arr = [1, 3, 2, 7, 4, 6]
	d = 2
	N = len(arr)

	# Function call
	arr = rotate(arr, d, N)
	for i in arr:
		print(i, end=" ")
