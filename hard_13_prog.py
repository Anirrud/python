def maxArea( A):
	l = 0
	r = len(A) -1
	area = 0
	while l < r:
		area = max(area, min(A[l],
						A[r]) * (r - l))
		if A[l] < A[r]:
			l += 1
		else:
			r -= 1
	return area
a = [1, 5, 4, 3]
print(maxArea(a))
b = [3, 1, 2, 4, 5]
print(maxArea(b))
c = [1,8,6,2,5,4,8,3,7]
print(maxArea(c))
d = [1,1]
print(maxArea(d))
e = [7,3] 
print(maxArea(e))
