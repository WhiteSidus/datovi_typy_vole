pole1 = [3, 2, 1, 5, 4]

def seradit(pole):
    for i in range(len(pole)):
        min_index = i
        for j in range(i+1, len(pole)):
            if pole[j] < pole[min_index]:
                min_index = j
        pole[i], pole[min_index] = pole[min_index], pole[i]

seradit(pole1)
print(pole1)