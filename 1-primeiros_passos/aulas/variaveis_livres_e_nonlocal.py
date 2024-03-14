# def primeira(a):
#     x=a*2
#     def segunda(b):
#         nonlocal x
#         x+=b
#         return x
#     return segunda

# concatenar= primeira('b')
# print(concatenar('c'))

def first(x):
    a=x
    def second():
        def thirth():
            nonlocal a
            a+=2
        thirth()
    second()
    return a

func= first(6)
print(func)