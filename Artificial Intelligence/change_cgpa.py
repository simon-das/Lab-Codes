dic = {}
fn = 'change_cgpa.txt'
print("\n")
f1=open(fn, "r")
for l in f1:
        name, dept, cgpa = l.split("\t")
        dic[name] = [dept, cgpa]
f1.close

for key, value in dic.items():
        name, dept, cgpa = key, value[0], value[1]
        print( name, '\t', dept, '\t', cgpa)

print("\n")
while True:
    name = input("Enter the name of whose cgpa you want to change : ")
    cgpa = str(input("Enter the new cgpa : "))
    cgpa = cgpa + "\n"
    dic[name][1] = cgpa
    ans = input("Do you want more changes(y/n) : ")
    if ans == 'n':
        break

f1=open(fn, "w")
for key, value in dic.items():
        name, dept, cgpa = key, value[0], value[1]
        s = name + "\t" + dept + "\t" + cgpa
        f1.write(s)
f1.close

print("\n")
f1=open(fn, "r")
for l in f1:
        name, dept, cgpa =l.split("\t")
        print(name, dept, cgpa, end="\n")
f1.close
