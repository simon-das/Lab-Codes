tupleList1=[('parent', 'Hasib', 'Rakib'),('parent', 'Rakib', 'Sohel'),
                ('parent', 'Hasib', 'Sakib'),('parent', 'Rakib', 'Rebeka'),
                ('parent', 'Rashid', 'Hasib'), ('parent', 'Hasib', 'Jarin')]
tupleList2=[('male', 'Hasib'),('male', 'Rakib'),('male', 'Sohel'),
            ('female', 'Rebeka'),('male', 'Rashid'), ('male', 'Sakib'),
            ('female', 'Jarin')]

# Procedure to find the brother of X

print("Finding brother")
X=str(input("First person:"))
print('Brother:', end=' ')
i=0
while(i<=5):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(6):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][1]) & ( tupleList1[j][2] != X)):
                for k in range(7):
                    if (tupleList2[k][0] == 'male') & (tupleList2[k][1] == tupleList1[j][2]):
                        print(tupleList1[j][2], end=' ')   
    i=i+1  



# Procedure to find the sister of X

print("\n\nFinding sister")
X=str(input("First person:"))
print('Sister:', end=' ')
i=0
while(i<=5):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(6):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][1]) & ( tupleList1[j][2] != X)):
                for k in range(7):
                    if (tupleList2[k][0] == 'female') & (tupleList2[k][1] == tupleList1[j][2]):
                        print(tupleList1[j][2], end=' ')   
    i=i+1



# Procedure to find the uncle of X

print("\n\nFinding uncle")
X=str(input("First person:"))
print('Uncle:', end=' ')
i = 0
i2 = 0
while(i<=5):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        while(i2<=5):
            if ((tupleList1[i2][0] == 'parent')&( tupleList1[i2][2] == tupleList1[i][1])):
                for j in range(6):
                    if ((tupleList1[j][0] == 'parent') & ( tupleList1[i2][1] == tupleList1[j][1]) & ( tupleList1[j][2] != tupleList1[i][1])):
                        for k in range(7):
                            if (tupleList2[k][0] == 'male') & (tupleList2[k][1] == tupleList1[j][2]):
                                print(tupleList1[j][2], end=' ')   
            i2=i2+1
    i=i+1



# Procedure to find aunty of X

print("\n\nFinding aunty")
X=str(input("First person:"))
print('Aunty:', end=' ')
i = 0
i2 = 0
while(i<=5):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        while(i2<=5):
            if ((tupleList1[i2][0] == 'parent')&( tupleList1[i2][2] == tupleList1[i][1])):
                for j in range(6):
                    if ((tupleList1[j][0] == 'parent') & ( tupleList1[i2][1] == tupleList1[j][1]) & ( tupleList1[j][2] != tupleList1[i][1])):
                        for k in range(7):
                            if (tupleList2[k][0] == 'female') & (tupleList2[k][1] == tupleList1[j][2]):
                                print(tupleList1[j][2], end=' ')   
            i2=i2+1
    i=i+1
    
