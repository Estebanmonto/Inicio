# print("Por favor ingrese la durción de la llamada")

# Minutos=float(input("Duración de la llamada en minutos: "))
# if Minutos >15:
#     print("la llamada tiene descuento del 20%")
# else:
#     print("no tiene descuento")

# Destino=str(input("Por favor ingrese el destino de la llamada: "))
# EstadosUnidos=900
# Canada=800
# Europa=950
# RestoMundo=1250

# if Minutos>15 and Destino=="Estados Unidos":
#     Costollamada=Minutos * EstadosUnidos
#     print(f'el valor de la llamada es {Costollamada*0.8}')
# elif Minutos>15 and Destino=="Canadá":
#     Costollamada=Minutos * Canada
#     print(f'el valor de la llamada es {Costollamada*0.8}')
# elif Minutos>15 and Destino=="Europa":
#     Costollamada=Minutos * Europa
#     print(f'el valor de la llamada es {Costollamada*0.8}')
# elif Minutos>15 and Destino=="Resto del mundo":
#     Costollamada=Minutos * RestoMundo
#     print(f'el valor de la llamada es {Costollamada*0.8}')
# elif Minutos<15 and Destino=="Estados Unidos":
#     Costollamada=Minutos * EstadosUnidos
#     print(f'el valor de la llamada es {Costollamada}')
# elif Minutos<15 and Destino=="Canadá":
#     Costollamada=Minutos * EstadosUnidos
#     print(f'el valor de la llamada es {Costollamada}')
# elif Minutos<15 and Destino=="Europa":
#     Costollamada=Minutos * Europa
#     print(f'el valor de la llamada es {Costollamada}')
# elif Minutos<15 and Destino=="Resto del mundo":
#     Costollamada=Minutos * RestoMundo
#     print(f'el valor de la llamada es {Costollamada}')


# print ('A continuacion debe ingresar el valor de la matricula ')

# matricula = float( input ( 'Valor de la matricula : '))

# print ('A continuacion debe ingresar las 4 notas de cada uno de los periodos ')

# periodo1 = float( input('Periodo 1 : '))  
# periodo2 = float( input('Periodo 2 : '))
# periodo3 = float( input('Periodo 3 : '))
# periodo4 = float( input('Periodo 4 :'))

# resultadoTotal = ((periodo1 + periodo2 + periodo3 + periodo4) / 4) 

# if resultadoTotal >=4 and resultadoTotal <=5:
#     print (f'El desempeño del alumno es Excelente, tiene un promedio de {resultadoTotal}')
#     print (f'El estudiante tiene un descuento de 20% en la matricula.')
#     print (f'El valor a pagar es de : {matricula*0.8}')
  
# elif resultadoTotal >=3 and resultadoTotal <=3.99:
#     print (f'El desempeño del alumno es Bien, tiene un promedio de {resultadoTotal}')
#     print (f'El estudiante debe pagar el total de la matricula.')
  
# elif resultadoTotal >=0 and resultadoTotal <=2.99:
#     print (f'El desempeño del alumno es Deficiente, tiene un promedio de {resultadoTotal}')
#     print (f'El estudiante debe pagar el total de la matricula.')


# print("Definir el medio de pago según el número de artículos")

# articulos=float(input("Por favor ingrese el número de artículos de su compra: "))
# if articulos<3:
#     print("Debe pagar en efectivo")
# else:
#     print("Debe pagar con tarjeta")


# numero1=float(input("Por favor ingrese el número 1: "))
# numero2=float(input("Por favor ingrese el número 2: "))
# numero3=float(input("Por favor ingrese el número 3: "))

# if numero1>numero2 and numero1>numero3:
#     print("El número 1 es mayor a número 2 y número 3")
# elif numero2>numero1 and numero2>numero3:
#     print("El número 2 es mayor a número 1 y número 3")
# elif numero3>numero1 and numero3>numero2:
#     print("El número 3 es mayor a número 1 y número 2")
# else:
#     print("No se puede definir el número mayor")

# print(f"Ingrese tres (3) números para saber cuál es el menor de estos y la suma de dichos:") 

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# num3 = int(input("Ingrese el tercer número: "))

# if num1 < num2 and num1 < num3:
#     print(f"El número menor es: {num1}")
# elif num2 < num1 and num2 < num3:   
#     print(f"El número menor es: {num2} ")
# elif num3 < num1 and num3 < num2:   
#     print(f"El número menor es: {num3}")

# suma = num1 + num2 + num3 

# print(f"La suma de sus números es: {suma}")


# horastrabajadas =float(input("Ingrese el número de horas trabajadas: "))
# valorhora=float(input("Ingrese el valor hora: "))

# if horastrabajadas > 40:
#     print("la tarifa se incrementa en un 50% para las horas extras")
# else:
#     print("se paga la tarifa regular")

# if horastrabajadas < 40:
#     Tarifa = horastrabajadas*valorhora
#     print(f'el salario es {Tarifa}')
# else:
#     Tarifa = (40*valorhora)+((horastrabajadas-40)*(valorhora*0.5))
#     print(f'el salario es {Tarifa}')

# cantidad = int(input("Ingresa la cantidad total de productos que adquiriste para determinar el descuento al que puedes acceder: "))

# if cantidad <= 3:
#     print(f"¡Tienes un descuento del 10% en tu total de compra!")
#     total = int(input("Ingresa el total de compra para asignarle tu nuevo descuento: $"))
#     descuento = total * 0.1
#     precio_final = total - descuento
#     print(f"El total a pagar es: {precio_final}")
# else:
#     print(f"¡Tienes un descuento del 20% en tu total de compra!")
#     total = int(input("Ingresa el total de compra para asignarle tu nuevo descuento: $"))
#     descuento = total * 0.2
#     precio_final = total - descuento
#     print(f"El total a pagar es: {precio_final}")

# print("Calcule el promedio de las siguientes calificaciones")
# print("Recuerde que las calificaciones son de 0 a 5")
# nota1=float(input("Ingrese el valor de la nota 1: "))
# nota2=float(input("Ingrese el valor de la nota 2: "))
# nota3=float(input("Ingrese el valor de la nota 3: "))
# nota4=float(input("Ingrese el valor de la nota 4: "))
# nota5=float(input("Ingrese el valor de la nota 5: "))

# promedio=(nota1+nota2+nota3+nota4+nota5)/5

# if promedio>=3:
#     print("El alumno aprueba el curso")
# else:
#     print("El alumno no aprueba el curso")

# Sueldo=float(input("Ingrese el valor del salario del trabajador: "))

# if Sueldo<=1000:
#     Descuento=Sueldo*0.10
#     print(f'El descuento del salario es {Descuento}, Total Salario es: {Sueldo-Descuento}')
# elif Sueldo<=2000:
#     Descuento=(Sueldo-1000)*0.05
#     print(f'El descuento del salario es {Descuento}, Total Salario es: {Sueldo-Descuento}')
# elif Sueldo>2000:
#     Descuento=(Sueldo-1000)*0.03
#     print(f'El descuento del salario es {Descuento}, Total Salario es: {Sueldo-Descuento}')


# print("Calcule el promedio de las siguientes calificaciones")
# print("Recuerde que las calificaciones son de 0 a 5")
# nota1=float(input("Ingrese el valor de la nota 1: "))
# nota2=float(input("Ingrese el valor de la nota 2: "))
# nota3=float(input("Ingrese el valor de la nota 3: "))
# nota4=float(input("Ingrese el valor de la nota 4: "))
# nota5=float(input("Ingrese el valor de la nota 5: "))

# promedio=(nota1+nota2+nota3+nota4+nota5)/5

# if promedio>=3:
#     print("El alumno aprueba el curso")
# else:
#     print("El alumno no aprueba el curso")

# print("Calcular el precio final de la moto")
# Preciomoto=float(input("Ingrese el valor de la motocicleta: "))
# Marca=str(input("Ingrese la marca de la moto: "))

# if Marca=="Honda":
#     Descuento=Preciomoto*0.05
#     Preciofinal=Preciomoto-Descuento
#     print(f'El precio de la moto es {Preciomoto}, El descuento es {Descuento}, El precio final es {Preciofinal}')
# elif Marca=="Yamaha":
#     Descuento=Preciomoto*0.08
#     Preciofinal=Preciomoto-Descuento
#     print(f'El precio de la moto es {Preciomoto}, El descuento es {Descuento}, El precio final es {Preciofinal}')
# elif Marca=="Suzuki":
#     Descuento=Preciomoto*0.1
#     Preciofinal=Preciomoto-Descuento
#     print(f'El precio de la moto es {Preciomoto}, El descuento es {Descuento}, El precio final es {Preciofinal}')
# else:
#     Descuento=Preciomoto*0.02
#     Preciofinal=Preciomoto-Descuento
#     print(f'El precio de la moto es {Preciomoto}, El descuento es {Descuento}, El precio final es {Preciofinal}') 

# numero = int(input("Ingresa un número para saber si este es par o impar: "))

# if numero % 2 == 0:
#     print("¡El número es par!")
# else:
#     print("¡El número es impar!")

# print(f"¿Sabías que tienes descuento dependiendo del día que compres tu moto?")
# compra_moto = input("Ingresa el día que compraste tu moto (Martes, Sádabo o Feriado): ")

# if compra_moto == 'Martes':
#     print(f"Tienes un 12% de descuento en tu compra")
#     compra_moto_martes = int(input("Ingresa el precio de tu moto para darte el nuevo valor: $"))
#     precio_moto_martes = compra_moto_martes - (compra_moto_martes * 0.12)
#     print(f"Tu nuevo valor es: ${precio_moto_martes}")
# elif compra_moto == 'Sábado':
#     print(f"Tienes un 18% de descuento en tu compra")
#     compra_moto_sabado = int(input("Ingresa el precio de tu moto para darte el nuevo valor: $")) 
#     precio_moto_sabado = compra_moto_sabado - (compra_moto_sabado * 0.18)
#     print(f"Tu nuevo valor es: ${precio_moto_sabado}")
# elif compra_moto == 'Feriado':
#     print(f"Tienes un 25% de descuento en tu compra")
#     compra_moto_feriado = int(input("Ingresa el precio de tu moto para darte el nuevo valor: $"))
#     precio_moto_feriado = compra_moto_feriado - (compra_moto_feriado * 0.25)
#     print(f"Tu nuevo valor es: ${precio_moto_feriado}")

