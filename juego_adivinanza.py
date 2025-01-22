import random



'''
   variables
   num 
   adivinaza = false
'''

print('Juego de adivinanza')
print('--------------------')

adivina_true = False
num_secreto = random.randint(1,100)
intentos=0

while not adivina_true:

    num = input('ingresa un numero entre 0 y 100: ')
    intentos+=1
    if num.isdigit():
        num = int(num)
        if num > num_secreto:
            print(f'el número {num} es mayor al numero secreto')
        elif num < num_secreto:    
            print(f'el número {num} es menor al numero secreto')
        else:
            print(f'Felicidades! ha adivinado el numero secreto en {intentos} intentos') 
            intentos=0   
    else:
        print(f'el valor {num} no es un numero valido ingrese un numero que este en rango de 1 y 100')
