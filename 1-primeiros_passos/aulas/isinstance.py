lista= [
    [0,3,5], 'Vítor', 12, 4.5, ('a','b'), {'Nome':'Vítor'},{5,6,4,3}
]
for item in lista:
    if isinstance(item, (int, float)):
        print(f'{item} é numérico')