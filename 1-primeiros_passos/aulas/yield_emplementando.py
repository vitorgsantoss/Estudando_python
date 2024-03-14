def generator(num=0):
    yield 1
    yield 2
    yield 3

gen= generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(gen)