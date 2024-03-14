l1= [1,3,4,5,6,9]
l2=[4,6,8,12,7]
def soma(l1,l2):
    iterator= min(len(l1),len(l2))
    resultado= [
        l1[i]+ l2[i] for i in range(iterator)
    ]
    return resultado
print(soma(l1,l2))