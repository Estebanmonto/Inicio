
# print ('Que funcion desea utilizar :')
# print ('1 = Hola mundo ')
# print ('2 = Suma de números ')
# print ('3 = Calcular la edad ')
# print ('4 = IMC (Indice de masa corporal ')
# print ('5 = Identificar de número par o impar ')
# print ('6 = Area de un cuadrado ')
# print ('7 = Area de un triangulo ')
# print ('8 = Mayor de edad o menor de edad ')
# print ('9 = Aumento del salario ')
# print ('10 = Pago de horas extras ')

# opcion = int(input(' ret : '))

# if opcion == 1:
#     print ('Hola mundo')

# if opcion == 2:
#     print ('SUMA DE NUMEROS')
#     numero1= float(input ('Digite el primer numero : '))
#     numero2 = float(input ('Digite el segundo numero : '))

#     print (f'La suma de los numeros {numero1} + {numero2} es igual a : {numero1+numero2}')

# if opcion == 3: 
    
#     import datetime

#     print ('CALCULADOR DE EDAD')
#     fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

#     fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
#     edad = datetime.datetime.now().year - fecha_nacimiento.year


#     print("Tu edad es:", edad)
    
# if opcion == 4:
#     peso = float(input("¿Desea conocer su índice de masa corporal (IMC)?  Ingrese aquí su peso (kg): "))
                   
#     altura = float(input("Ingrese su altura: "))

#     imc = peso / (altura ** 2)      

#     if imc < 18.5:  
#         print(f"Su índice de masa corporal es inferior al normal.")

#     elif imc >= 18.5 and imc < 24.9:
#         print(f"Su índice de masa corporal es normal.")

#     elif imc > 25 and imc <= 29.9:
#         print(f"Su índice de masa corporal es superior al normal.")

#     else:
#         print(f"Usted está bojudo.")

# if opcion == 5:
#     print ('NUMERO PAR O IMPAR')
#     numero = float( input ('Ingrese el numero : '))

#     if numero == 0:
#         print('El numero es 0')

#     elif numero % 2 == 0:
#         print('El numero es par')
        
#     else:
#         print('El numero no es par')
    
# if opcion == 6:
#     print ('AREA DE UN CUADRADO')
#     print ('La formula de un cuadrado es igual a Lado x Lado')
#     lado = float( input (f'Ingrese el Lado : '))
#     print (f'Area del cuadrado : {lado*lado}')
    
# if opcion == 7:
#     print ('AREA DE UN TRIANGULO')
#     print ('La formula de un triangulo es base * altura / 2')

#     base = float( input ('Ingrese la base : '))
#     altura = float( input ('Ingrese la altura : '))

#     print (f'Area del triangulo : {base * altura / 2} ')
    
# if opcion == 8:
#     print()
#     print("CALCULAR SI ERES MAYOR DE EDAD")

#     resultado = int(input ("¿Cuál es tu edad?: "))

#     if resultado >=0 and resultado <=5:
#         print ("Eres menor de edad. Estás en la primera infancia.")
#     elif resultado >=6 and resultado <=18:
#         print ("Eres menor de edad. Estás en la adolescencia.")
#     elif resultado >=19 and resultado <=60:
#         print ("Eres mayor de edad. Estás en la adultez.")
#     elif resultado >61:
#         print ("Eres mayor de edad. Estás en la tercera edad." )
               
# if opcion == 9:
#     print()
#     print('CALCULAR AUMENTO DE SALARIO')

#     salario = int(input('Ingresa tu salario actual para saber si obtendrás un aumento de este para el siguiente periodo: $'))

#     if salario > 1160000:
#         print('Obtendrás un aumento en el salario')
#     else:
#         print('No obtendrás un aumento en el salario')

# if opcion == 10:
#     print ()
#     print ('PAGO DE HORAS EXTRAS')
#     print ('La jornada laboral es de 40 horas')
#     print ('Si se trabajan horas adicionales, se aplicara un recargo del 1.5 por cada hora extra')
#     hrs = input("Ingrese las horas laboradas: ")
#     h = float(hrs)
#     rph = input("Valor por hora: ")
#     r = float(rph)

#     if h>40:    
#         normalh=40*r    
#         extrah = (h-40)*(r*1.5)  
#         pay = normalh + extrah
#         print(pay)
#     else:
#         pay = h*r
#         print(pay)

    
    

# print ('Que funcion desea utilizar :')
# print ('1 = Hola mundo ')
# print ('2 = Suma de números ')
# print ('3 = Calcular la edad ')
# print ('4 = IMC (Indice de masa corporal ')
# print ('5 = Identificar de número par o impar ')
# print ('6 = Area de un cuadrado ')
# print ('7 = Area de un triangulo ')


# opcion = int(input(' ret : '))

# if opcion == 1:
#     print ('Hola mundo')

# if opcion == 2:
#     print ('SUMA DE NUMEROS')
#     numero1= float(input ('Digite el primer numero : '))
#     numero2 = float(input ('Digite el segundo numero : '))

#     print (f'La suma de los numeros {numero1} + {numero2} es igual a : {numero1+numero2}')

# if opcion == 3: 
    
#     import datetime

#     print ('CALCULADOR DE EDAD')
#     fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

#     fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
#     edad = datetime.datetime.now().year - fecha_nacimiento.year


#     print("Tu edad es:", edad)
    
# if opcion == 4:
#     peso = float(input("¿Desea conocer su índice de masa corporal (IMC)?  Ingrese aquí su peso (kg): "))
                   
#     altura = float(input("Ingrese su altura: "))

#     imc = peso / (altura ** 2)      

#     if imc < 18.5:  
#         print(f"Su índice de masa corporal es inferior al normal.")

#     elif imc >= 18.5 and imc < 24.9:
#         print(f"Su índice de masa corporal es normal.")

#     elif imc > 25 and imc <= 29.9:
#         print(f"Su índice de masa corporal es superior al normal.")

#     else:
#         print(f"Usted está bojudo.")

# if opcion == 5:
#     print ('NUMERO PAR O IMPAR')
#     numero = float( input ('Ingrese el numero : '))

#     if numero == 0:
#         print('El numero es 0')

#     elif numero % 2 == 0:
#         print('El numero es par')
        
#     else:
#         print('El numero no es par')
    
# if opcion == 6:
#     print ('AREA DE UN CUADRADO')
#     print ('La formula de un cuadrado es igual a Lado x Lado')
#     lado = float( input (f'Ingrese el Lado : '))
#     print (f'Area del cuadrado : {lado*lado}')
    
# if opcion == 7:
#     print ('AREA DE UN TRIANGULO')
#     print ('La formula de un triangulo es base * altura / 2')

#     base = float( input ('Ingrese la base : '))
#     altura = float( input ('Ingrese la altura : '))

#     print (f'Area del triangulo : {base * altura / 2} ')
    

# numeros = [1, 2, 4, 5]
# numeros.append(3)
# print(numeros)


# dictionary = {"key1":"value1", "key2":"value2", "key3":"value3"}
# print(dictionary)
# dictionary["key4"] = "value4"
# print(dictionary)
# dictionary["key2"] = "value4"
# print(dictionary)

# info = {1, 2, 3, 4, 5}
# info.add(6)
# print(info)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# a | b
# {1, 2, 3, 4, 5, 6}

# a & b
# {3, 4}

# a = {1, 2, 3, 4}
# b = {2, 3}
# a - b
# {1, 4}

# {1, 2, 3} == {3, 2, 1}
# True
# {1, 2, 3} == {4, 5, 6}
# False
