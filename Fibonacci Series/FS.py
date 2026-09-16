def fib_series(nterms):
    n1,n2 = 0,1
    count=0
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
nterms=int(input("How many terms?"))
if nterms<=0:
    print("Please Enter a Positive Integer")
elif nterms==1:
    print("Fibonacci Sequence upto", nterms,":")
    fib_series(nterms)
else:
    print("Fibonacci sequence:")
    fib_series(nterms)