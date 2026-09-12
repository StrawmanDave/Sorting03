import random

def main():
    
    #put sorting alg into a list
    random_list = createRandomList(10)
    algorithmList = [bubbleSort(random_list), shakerSort(random_list), countingSort(random_list), mergeSort(random_list), quickSort(random_list), modQuickSort(random_list)]

    #Main function should loop through the data sizes 8 - 4k that is 2^3 and 2^12
    
    
    #run each alg thourgh measuring work
    #work is a data compare or data swap/move
    #size of the chart is on the outside when making the table
    
    #do it again with mostly sorted data
    #create a mostly sorted function

    #make the oupt of these be tables

    #then tkae dat into a sheet software that can create a line chart

    #makea log log chare meaing a char that scales by 2^N

main()

def mostlySortedList(size)
    A_list = createRandomList(size)
    A_list.sort()
    A_list[0], A_list[size] = A_list[size], A_list[0]
    return A_list

def createRandomList(size):
    # create a list with A number of integers so 0-9 as the index.
    b = []
    for i in range(size):
        b.append(random.randrange(0, size))
    return b

def bubbleSort(A):
        is_Sorted = False
        while is_Sorted == False:
            is_Sorted = True
            for i in range(len(A) - 1):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    is_Sorted = False

def shakerSort(A):
    is_Sorted = False
    while is_Sorted == False:
        is_Sorted = True
        for i in range(len(A) - 1):
              if A[i] > A[i + 1]:
                   A[i], A[i + 1] = A[i + 1], A[i]
                   is_Sorted = False
        for i in range(len(A) -2, -1, -1):
             if A[i] > A[i + 1]:
                  A[i], A[i + 1] = A[i + 1], A[i]
                  is_Sorted = False

def countingSort(A):
    # print (A) 
    f = [0] * len(A)
    # print(f)

    for x in A:
        f[x] = f[x] + 1 # finds the iteration of the given number and adds one to it.
    # print(f)

    K = 0 # initialize k first to be zero so it does not throw errors
    for i in range(len(f)): 
         v = i # v is the value you are on
         count = f[i] # count is how many there are of that value
         for j in range(count): # this loop will only do anything if the count is bigger than 0
            # print(j, end=" ")
            A[K] = v #A[K] starts at zero goes up
            K += 1 # we use k to iterate up becuase if we use j it will be an error out of the range

def mergeSort(A):
    k = 0
    i = 0
    j = 0
    # Base case
    if(len(A) <= 1):
        return
    # Split the list into 2
    x = len(A)//2
    L = A[0:x]
    R = A[x:len(A)]
    # Sort L and R
    mergeSort(L)
    mergeSort(R)
    # 3 varible loop
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
            k += 1
        else:
            A[k] = R[j]
            j += 1
            k += 1
        if i < len(L) and j == len(R):
             while i < len(L):
                A[k] = L[i]
                i += 1
                k += 1
    if j < len(R) and i == len(L):
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

def quickSortR(A, low, high, mod):
    if high - low == 0:
        return
    # modified part
    if mod == True:
        mid = (low + high)//2
        A[low], A[mid] = A[mid], A[low]
    lmgt = low + 1
    
    for i in range(low + 1 , high, 1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]
    quicksortr(A, low, pivot, False)
    quicksortr(A, pivot + 1, high, False)

def quickSort(A):
    quickSortR(A, 0, len(A), False)

def modQuickSort(A):
    quickSortR(A, 0, len(A), True)

