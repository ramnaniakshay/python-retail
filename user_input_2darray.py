import numpy as np

rows  = int(input("Enter the number of rows: "))
cols  = int(input("Enter the number of cols: "))

            
array = np.zeros((rows,cols))

print("Enter the elements row wise")

for i in range(rows):
            for j in range(cols):
                array[i][j] = int(input())

print("2 d array is as below")
print(array)
