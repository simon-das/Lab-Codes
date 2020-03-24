queens = [(1, 2), (1, 8), (3, 6), (4, 5), (5, 3), (6, 1), (7, 4), (8, 7)]

count = 0
for i in range(8):
    for j in range(8):
        #checking in right side
        if queens[j][1] > queens[i][1] :
            #checking horizontally
            if queens[i][0] == queens[j][0]:
                count += 1
            #checking diagonally
            elif abs(queens[j][0] - queens[i][0]) == abs(queens[j][1] - queens[i][1]):
                count += 1

print('Heuristics : ', count)
