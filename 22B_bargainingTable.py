n,m = map(int,raw_input().split())
a = [raw_input() for i in range(n)]
ans = 0

#Solution 1
#by traversing every possible submatrix and finding the answer which is the perimeter
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1,n):
            for y2 in range(y1,m):
                flag = True
                for i in range(x1,x2+1):
                    for j in range(y1,y2+1):
                        if a[i][j] == '1':
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    ans = max(ans,2*((x2-x1+1)+(y2-y1+1)))
print ans

'''
#Solution to find the area efficiently
a = [[int(x) for x in y] for y in a]

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            a[i][j] = 1
        else:
            a[i][j] = 0

#O(n^2)
def maxHistogramArea(height):
    n = len(height)
    if n == 0:
        return 0

    maxArea = 0
    for i in range(n):
        minHeight = height[i]
        maxArea = max(maxArea,minHeight)
        for j in range(i+1,n):
            minHeight = min(minHeight,height[j])
            maxArea = max(maxArea,minHeight*(j-i+1))
    return maxArea

#O(n) using stack
def largestRectangleArea(A):
    ans = 0
    A = [-1] + A
    A.append(-1)
    n = len(A)
    stack = [0]  # store index

    for i in range(n):
        while A[i] < A[stack[-1]]:
            h = A[stack.pop()]
            area = h*(i-stack[-1]-1)
            ans = max(ans, area)
        stack.append(i)
    return ans

def maxRect(a):
    result = maxHistogramArea(a[0])
    for i in range(1,n):
        for j in range(m):
            if a[i][j]:
                a[i][j] += a[i-1][j]
        result = max(result,maxHistogramArea(a[i]))
    return result
print maxRect(a)
'''





                    
