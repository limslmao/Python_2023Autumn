#python

a = [[1,2,4], [3,5,7], [2,4,9]]
# 1 2 4
# 3 5 7
# 2 4 9
b = [[1]*3 for row in range(3)]
# 1 1 1
# 1 1 1
# 1 1 1


c = [[None]*3 for row in range(3)]
# '' '' ''
# '' '' ''
# '' '' ''

#matrix addition
for i in range(3):
    for j in range(3):
        c[i][j] = a[i][j]+b[i][j]

#print
print("a矩陣與b矩陣相加後為：")
for row in range(3):
    for col in range(3):
        print(c[row][col], end='\t')
    print("") 