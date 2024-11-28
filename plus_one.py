def plus_one(A):
    A[-1] += 1 #Increment the last digit by one
    for i in reversed(range(1, len(A))):
        print("H1",A)
        if A[i] != 10:
            break
        print("H2",A)
        A[i] = 0
        print("H3",A)
        A[i-1] += 1
        print("H4",A)

    if A[0] == 10:
        print("H5",A[0])
        A[0] = 1
        print("H6",A)
        A.append(0)
        print("H7",A)

    return A

plus_one([9,9,9])