def sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
        return True
    

# giving input for the list
arr=list(map(int,input("enter the list of array:").split()))


#calling the function 
print(sorted(arr))