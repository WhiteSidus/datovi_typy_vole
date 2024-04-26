pole = [3,2,1,5,4]

def srovnat(vstup):
    for x in range(len(vstup)):
        for y in range(len(vstup)):
            if x >= y:

            elif x < y:
            vstup[x] = vstup[(len(vstup)) - 1] 

            else:
                vstup[x] = vstup[y]
                vstup.pop(vstup[x])
                break

srovnat(pole)