# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)

def sum (x):
    sum = 0
    for i in range(x+1):
        sum = sum + i
    return sum

