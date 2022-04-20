def int_input():
    return list(map(int,input().split()))
def binary_search(arr, x): #Algo to search a number in 1-D Sorted array
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
[m , n] = int_input()
[k] = int_input()
arr = []
for _ in range(m):
    #Converting Matrix to List of Sorted Elements
    for x in list(map(int,input().split())):
        arr.append(x)
ind = binary_search(arr,k)+1 # Position to value in list
if ind !=0:
    #Converting Postion in List to Position in Matrix
    i=int(ind/n)
    j = ind - n*i -1
    print("True")
    print(i,j)
else:
    print("False")
