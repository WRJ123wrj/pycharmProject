score=int(input('分数：'))

if score>=90:
    grade='A'
elif score>=60:
    grade='B'
else:
    grade='C'

print('属于%s等' %grade)