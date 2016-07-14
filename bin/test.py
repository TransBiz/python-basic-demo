import os
from basic import gen_x, mem

X0 = float(os.environ.get("X0",1.))
M = int(os.environ.get("M",20))

x = gen_x(X0)

for m in range(M):
    print "x("+str(m)+") = ", x(m)

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


@mem
def fib(n):
    return 1 if n < 2 else fib(n-1)+fib(n-2)


for m in range(M):
    print "fib("+str(m)+") = ", fib(m)

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


@mem
def mfib(n):
    return 1 if n < 2 else mfib(n-1)+mfib(n-2)+mfib(n-3)


for m in range(M):
    print "mfib("+str(m)+") = ", mfib(m)




