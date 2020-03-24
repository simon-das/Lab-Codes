gtp=[(1,1,1), (2,1,2), (3,1,3), (4,2,3), (5,3,3), (6,3,2), (7,3,1), (8,2,1)]
gblnk = (2,1)
tp=[(1,1,2), (2,1,3), (3,2,1), (4,2,3), (5,3,3), (6,2,2), (7,3,2), (8,1,1)]
blnk = (3,1)

# Procedure to find the manhattan distance
i,h=0,0
while(i<=7):
    h = h + abs(tp[i][1] - gtp[i][1]) + abs(tp[i][2] - gtp[i][2])  
    i=i+1
print('Heuristics : ',h)
