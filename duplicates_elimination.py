def eliminating_duplicates(arr):
    i=0
    for j in range(2,len(arr)):
        if arr[i] != arr[j]:
            i+=1
            arr[i]=arr[j]
    return i+1

arr=[1,1,2,3,3,3,4,5,6,6]
a = eliminating_duplicates(arr)
