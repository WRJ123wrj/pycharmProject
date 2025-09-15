y=int(input('year='))
m=int(input('month='))
d=int(input('day='))

sum=0
months=[0,31,59,90,120,151,181,212,243,273,304,334]
if 0<m<=12:
    sum=months[m-1]
else:
    print('日期错误')
sum+=d

leap=0
if(y%400==0)or((y%4==0)and(y%100!=0)):
    leap=1
if(leap==1)and(m>2):
    sum+=1
print('这是第%d天'%sum)
