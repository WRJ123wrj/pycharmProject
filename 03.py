def find_number():
    for i in range(2,85):
        if 168%i==0:
            j=168//i
            if i>j and (i+j)%2==0:
                m=(i+j)//2
                n=(i-j)//2
                x=n*n-100
                print(x)

find_number()
