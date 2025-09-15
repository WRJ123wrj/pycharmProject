a=[1,5,10,61,78]

num=int(input("输入一个数字："))
k=0
for i in range(len(a)):
    if(num>a[i]):
        k=i+1
    else:
        break
a.insert(k,num)
print("插入后的数组：",a)