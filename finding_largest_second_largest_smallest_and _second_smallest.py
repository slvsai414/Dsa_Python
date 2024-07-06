def number(l):
    largest = float('-inf')

    sec_largest = 0
    
    smallest = float('inf')

    sec_smallest = float('inf')

    for i in range(len(l)):
        #checking it's a large number or not
        if l[i] > largest:

            #upadating second largest number
            sec_largest = largest

            #updating largest number
            largest = l[i]

            #checking for anthor test case where it will not enter the if condition
        elif l[i] > sec_largest and l[i] != largest:
            sec_largest = l[i]

        #checking for smaller elements in array

        if l[i] < smallest:
            sec_smallest = smallest
            smallest = l[i]
        #checking for anthor testcase to find the sec smallest 
        elif l[i] < sec_smallest and l[i] != smallest:
            sec_smallest = l[i]
    return largest,sec_largest,smallest,sec_smallest

# giving the input to the list
l=list(map(int,input().split()))

# calling the function 
print(number(l))



