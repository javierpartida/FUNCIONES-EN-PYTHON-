import streamlit as st

# Funciones de los ejercicios
def saludar(nombre):
    return f"Hola, {nombre}!"

def sumar(a, b):
    return a + b

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * descuento / 100)
    return precio_descuento + (precio_descuento * impuesto / 100)

def sumar_lista(numeros):
    return sum(numeros)

def producto(nombre, cantidad=1, precio=10):
    return f"{nombre}: Total a pagar: {cantidad * precio}"

def numeros_pares_e_impares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado if args else 1

def informacion_personal(**kwargs):
    return kwargs

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

# Interfaz Streamlit
st.title("Ejercicios con Funciones en Python")

opcion = st.sidebar.selectbox(
    'Selecciona un ejercicio',
    ('Saludo', 'Suma de Dos Numeros', 'Area de un Triangulo', 'Calculadora de Descuento',
     'Suma de Lista', 'Producto con Valores Predeterminados', 'Pares e Impares', 
     'Multiplicacion con *args', 'Informacion Personal', 'Calculadora Flexible'))

if opcion == 'Saludo':
    nombre = st.text_input("Nombre:")
    if nombre:
        st.write(saludar(nombre))

elif opcion == 'Suma de Dos Numeros':
    num1 = st.number_input("Numero 1:", value=0)
    num2 = st.number_input("Numero 2:", value=0)
    if st.button("Sumar"):
        st.write(sumar(num1, num2))

elif opcion == 'Area de un Triangulo':
    base = st.number_input("Base:", value=0)
    altura = st.number_input("Altura:", value=0)
    if st.button("Calcular Area"):
        st.write(calcular_area_triangulo(base, altura))

elif opcion == 'Calculadora de Descuento':
    precio = st.number_input("Precio:", value=0)
    descuento = st.number_input("Descuento:", value=10)
    impuesto = st.number_input("Impuesto:", value=16)
    if st.button("Calcular Precio Final"):
        st.write(calcular_precio_final(precio, descuento, impuesto))

elif opcion == 'Suma de Lista':
    numeros = st.text_input("Lista de numeros separados por comas:")
    if numeros:
        lista = [int(n) for n in numeros.split(',')]
        st.write(sumar_lista(lista))

elif opcion == 'Producto con Valores Predeterminados':
    nombre_producto = st.text_input("Producto:")
    cantidad = st.number_input("Cantidad:", value=1)
    precio = st.number_input("Precio:", value=10)
    if st.button("Calcular Total"):
        st.write(producto(nombre_producto, cantidad, precio))

elif opcion == 'Pares e Impares':
    numeros = st.text_input("Lista de numeros separados por comas:")
    if numeros:
        lista = [int(n) for n in numeros.split(',')]
        pares, impares = numeros_pares_e_impares(lista)
        st.write(f"Pares: {pares}")
        st.write(f"Impares: {impares}")

elif opcion == 'Multiplicacion con *args':
    numeros = st.text_input("Numeros separados por comas:")
    if numeros:
        lista = [int(n) for n in numeros.split(',')]
        st.write(f"Resultado: {multiplicar_todos(*lista)}")

elif opcion == 'Informacion Personal':
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad:", value=0)
    direccion = st.text_input("Direccion:")
    if st.button("Mostrar Informacion"):
        info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion)
        st.write(info)

elif opcion == 'Calculadora Flexible':
    num1 = st.number_input("Numero 1:", value=0)
    num2 = st.number_input("Numero 2:", value=0)
    operacion = st.selectbox("Operacion:", ['suma', 'resta', 'multiplicacion', 'division'])
    if st.button("Calcular"):
        st.write(f"Resultado: {calculadora_flexible(num1, num2, operacion)}")
