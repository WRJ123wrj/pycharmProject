length=int(input('输入数组长度'))

a=[]
print('依次输入数字')
for i in range(length):
    x=int(input())
    a.append(x)

for j in range(length//2):
    a[j],a[length-j-1]=a[length-j-1],a[j]
    print(a)
