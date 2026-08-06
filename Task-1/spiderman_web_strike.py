#spiderman web launch

matrix = [[1,0,0,0,1], [1,0,1,1,1],[1,1,0,1,1],[1,0,1,1,0],[0,1,0,1,1]]

n = len(matrix)
m = 3
rad = m//2

#directions = [(-1,0)]
max_count = 0
best_cord  = []
best_criminals = []

for row in range(rad, n - rad):
    for col in range(rad, n - rad ):
        if matrix[row][col] == 0:
            continue
        
        else:
            count = 0
            criminals =[]

            for i in range(row - rad, row +rad + 1):
                for j in range(col - rad, col + rad + 1):
                    if matrix[i][j] == 1:
                        count+=1

                        x= j
                        y = n - 1 - i

                        criminals.append((x,y))

            if count > max_count:
                max_count = count
                #best_cord = (row,col)
                best_cord = (col,n-1-row)

                best_criminals = criminals.copy()

print("Best Launch Coordinate: ",best_cord)
print("Maxinmum Criminals Captured: ",max_count)
print("Coordinates of criminals: ",best_criminals)
                        