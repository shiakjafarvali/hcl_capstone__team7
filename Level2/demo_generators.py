def demo():
    yield 'A'
    yield 'B'
    yield 'C'
x=demo()
print(next(x))
print(next(x))
num=[x * x for x in range(10000)]
print(num)