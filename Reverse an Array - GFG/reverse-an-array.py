#code


def reverse(N, A):
    
    start = 0
    end = N-1
    
    while start < end:
        A[start], A[end] = A[end], A[start]
        start+=1
        end-=1

    
if __name__=='__main__':
    T = int(input())
    while T:
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        reverse(sizeOfArray, arr)
        for i in arr:
            print(i, end=" ")
        print('')
        T-=1
        