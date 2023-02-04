testCase = int(input())         # take input for number of testcase convert to integer
for sentence in range (0,testCase):     # loop through each testcase
    A = input()
    list_A = list(A)                    # A, B use to take input from user, C equal a list same as A
    B = input()
    list_B = list(B)
    C = list_A
    for i in range(0,len(list_A)):      # check each index of A and B, if they are same, replace that index of C
        if A[i] == B[i]:                # with "."  else replace with "*"
            C[i] = "."
        else:
            C[i] = "*"
    myString = ""                       # after we get C, we want return it back to string
    for x in C:
        myString += x
    print(A)                            # print everything out
    print(B)
    print(myString)
    print()