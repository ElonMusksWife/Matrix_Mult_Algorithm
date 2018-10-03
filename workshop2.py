A = []
a = []
B = []
b = []

print("type the size of matrix 1")

size_of_matrix_1r = int(input()) #number of rows
size_of_matrix_1c = int(input()) #number of columns

print("type the size of matrix 2")

size_of_matrix_2r = int(input()) #number of rows
size_of_matrix_2c = int(input()) #number of columns

if (size_of_matrix_1c!=size_of_matrix_2r):
    print("matrices will not be multiplied")

print("")

try:
    while(len(a)!=size_of_matrix_1c):
        for i in range(size_of_matrix_1r):
            a=[int(x) for x in input().split()]
            if len(a)!= size_of_matrix_1c:
                print("")
            A.append(a)

except IndexError:
    pass

try:
    while(len(b)!=size_of_matrix_2c):
        for i in range(size_of_matrix_2r):
            b=[int(x) for x in input().split()]
            if len(b)!= size_of_matrix_2c:
                print("")
            A.append(b)

except IndexError:
    pass

result = [[0 for x in range(size_of_matrix_2c) for i in range(size_of_matrix_1r)]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            try:
                result[i][j] += A[i][k] * B[k][j]
            except IndexError:
                pass















