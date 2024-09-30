import streamlit as st  # Importamos la libreria de Streamlit para crear la interfaz grafica

# Definimos las funciones para cada ejercicio

# Funcion 1: Saludar
def saludar(nombre):
    return f"Hola, {nombre}!"

# Funcion 2: Sumar dos numeros
def sumar(a, b):
    return a + b

# Funcion 3: Calcular el area de un triangulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Funcion 4: Calculadora de descuento
def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * descuento / 100)  # Aplicamos descuento
    return precio_descuento + (precio_descuento * impuesto / 100)  # Sumamos el impuesto

# Funcion 5: Sumar una lista de numeros
def sumar_lista(numeros):
    return sum(numeros)  # Sumamos todos los elementos de la lista

# Funcion 6: Calcular el costo total de un producto con valores predeterminados
def producto(nombre, cantidad=1, precio=10):
    return f"{nombre}: Total a pagar: {cantidad * precio}"

# Funcion 7: Separar numeros pares e impares
def numeros_pares_e_impares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares

# Funcion 8: Multiplicar todos los numeros usando *args
def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado if args else 1

# Funcion 9: Mostrar informacion personal usando **kwargs
def informacion_personal(**kwargs):
    return kwargs  # Devuelve la informacion en formato clave: valor

# Funcion 10: Calculadora flexible que realiza diferentes operaciones
def calculadora_flexible(num1, num2, operacion='suma'):
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'multiplicacion':
        return num1 * num2
    elif operacion == 'division':
        return num1 / num2 if num2 != 0 else "No se puede dividir entre cero"
    return "Operacion no valida"

# Interfaz principal con Streamlit

st.title("Ejercicios con Funciones en Python")  # Titulo de la aplicacion

# Barra lateral para seleccionar entre los diferentes ejercicios
opcion = st.sidebar.selectbox(
    'Selecciona un ejercicio',
    ('Saludo', 'Suma de Dos Numeros', 'Area de un Triangulo', 'Calculadora de Descuento',
     'Suma de Lista', 'Producto con Valores Predeterminados', 'Pares e Impares', 
     'Multiplicacion con *args', 'Informacion Personal', 'Calculadora Flexible'))

# Segun la opcion seleccionada, mostramos los inputs correspondientes y los resultados

# Ejercicio 1: Saludo
if opcion == 'Saludo':
    nombre = st.text_input("Nombre:")  # Recibimos el nombre del usuario
    if nombre:
        st.write(saludar(nombre))  # Mostramos el saludo personalizado

# Ejercicio 2: Suma de dos numeros
elif opcion == 'Suma de Dos Numeros':
    num1 = st.number_input("Numero 1:", value=0)  # Primer numero
    num2 = st.number_input("Numero 2:", value=0)  # Segundo numero
    if st.button("Sumar"):  # Boton para realizar la suma
        st.write(sumar(num1, num2))  # Mostramos el resultado

# Ejercicio 3: Area de un triangulo
elif opcion == 'Area de un Triangulo':
    base = st.number_input("Base:", value=0)  # Base del triangulo
    altura = st.number_input("Altura:", value=0)  # Altura del triangulo
    if st.button("Calcular Area"):  # Boton para calcular el area
        st.write(calcular_area_triangulo(base, altura))  # Mostramos el resultado

# Ejercicio 4: Calculadora de descuento
elif opcion == 'Calculadora de Descuento':
    precio = st.number_input("Precio:", value=0)  # Precio original
    descuento = st.number_input("Descuento:", value=10)  # Descuento en porcentaje
    impuesto = st.number_input("Impuesto:", value=16)  # Impuesto en porcentaje
    if st.button("Calcular Precio Final"):  # Boton para calcular el precio final
        st.write(calcular_precio_final(precio, descuento, impuesto))  # Mostramos el resultado

# Ejercicio 5: Suma de lista de numeros
elif opcion == 'Suma de Lista':
    numeros = st.text_input("Lista de numeros separados por comas:")  # Recibimos la lista como texto
    if numeros:
        lista = [int(n) for n in numeros.split(',')]  # Convertimos la lista de texto a enteros
        st.write(sumar_lista(lista))  # Mostramos la suma

# Ejercicio 6: Producto con valores predeterminados
elif opcion == 'Producto con Valores Predeterminados':
    nombre_producto = st.text_input("Producto:")  # Nombre del producto
    cantidad = st.number_input("Cantidad:", value=1)  # Cantidad a comprar
    precio = st.number_input("Precio:", value=10)  # Precio por unidad
    if st.button("Calcular Total"):  # Boton para calcular el total
        st.write(producto(nombre_producto, cantidad, precio))  # Mostramos el total

# Ejercicio 7: Pares e Impares
elif opcion == 'Pares e Impares':
    numeros = st.text_input("Lista de numeros separados por comas:")  # Recibimos la lista de numeros
    if numeros:
        lista = [int(n) for n in numeros.split(',')]  # Convertimos a enteros
        pares, impares = numeros_pares_e_impares(lista)  # Separamos pares e impares
        st.write(f"Pares: {pares}")  # Mostramos los numeros pares
        st.write(f"Impares: {impares}")  # Mostramos los numeros impares

# Ejercicio 8: Multiplicacion con *args
elif opcion == 'Multiplicacion con *args':
    numeros = st.text_input("Numeros separados por comas:")  # Recibimos la lista de numeros
    if numeros:
        lista = [int(n) for n in numeros.split(',')]  # Convertimos a enteros
        st.write(f"Resultado: {multiplicar_todos(*lista)}")  # Mostramos el resultado de la multiplicacion

# Ejercicio 9: Informacion Personal con **kwargs
elif opcion == 'Informacion Personal':
    nombre = st.text_input("Nombre:")  # Nombre de la persona
    edad = st.number_input("Edad:", value=0)  # Edad
    direccion = st.text_input("Direccion:")  # Direccion
    if st.button("Mostrar Informacion"):  # Boton para mostrar la informacion
        info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion)  # Pasamos los datos
        st.write(info)  # Mostramos la informacion

# Ejercicio 10: Calculadora Flexible
elif opcion == 'Calculadora Flexible':
    num1 = st.number_input("Numero 1:", value=0)  # Primer numero
    num2 = st.number_input("Numero 2:", value=0)  # Segundo numero
    operacion = st.selectbox("Operacion:", ['suma', 'resta', 'multiplicacion', 'division'])  # Seleccion de operacion
    if st.button("Calcular"):  # Boton para calcular
        st.write(f"Resultado: {calculadora_flexible(num1, num2, operacion)}")  # Mostramos el resultado
