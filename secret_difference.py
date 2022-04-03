nums = [int(x) for x in input()]

A=0
B=0
for i in range(1,len(nums),2):
	A = A+nums[i]
for i in range(0,len(nums),2):
	B = B+nums[i]
c = abs(A-B)
print(c)	
