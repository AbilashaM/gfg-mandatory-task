n=int(input("Enter the number:"))
s=0
num=n
while(n!=0):
 r=n%10
 s=s+(r*r*r)
 n=int(n/10)
if(s==num):
 print("the number is armstrong")
else:
    print("the number is not armstrong")