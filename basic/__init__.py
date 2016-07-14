
fib = lambda n: 1 if n < 2 else fib(n-1) + fib(n-2)


def gen_x(x0):
    x = lambda n: x0 if n < 2 else 1. + 1./(x(n-1)+1)
    return x


def mem(f):
    res = {}
    def new_f(n):
        if n not in res:
            res[n] = f(n)
        return res[n]
    return new_f

