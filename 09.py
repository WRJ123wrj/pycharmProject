a=[]
sum=0

for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(int(input("输入数字：")))
for k in range(3):
    sum+=a[k][k]
print(sum)
