def recursiva(num,fat=1):
    fat*= num
    num-=1
    if num == 1:
        return fat
    else:
        return recursiva(num,fat)
    
print(recursiva(3))