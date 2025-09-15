i=int(input('净利润为：'))
arr=[300000,200000,100000,0]
rat=[0.010,0.050,0.075,0.100]
r=0
for money in range(0,4):
    if i>arr[money]:
        r+=(i-arr[money])*rat[money]
        print((i-arr[money])*rat[money])
        i=arr[money]
print('最终奖金总额：')
print(r)
