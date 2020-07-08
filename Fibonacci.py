#Program to print Fibonacci numbers

n1=0
n2=1
i=0
n=int(input("Enter the number of terms "))
if n<=0:
      print("Enter positive numbers")
elif n==1:
    print("Fibonacci series:\n")
    print(n1)
else:
    print("Fibonacci series:\n")
    while i<n:
        print(n1)
        s=n1+n2
        n1=n2
        n2=s
        i=i+1
