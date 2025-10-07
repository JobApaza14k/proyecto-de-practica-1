# Método de Newton-Raphson donde el usuario escribe la función

print("=== MÉTODO DE NEWTON-RAPHSON ===")
print("Ejemplo: para x^3 - 4*x + 1 escribe: x**3 - 4*x + 1\n")


funcion_str = input("Ingresa la función f(x): ")
derivada_str = input("Ingresa la derivada f'(x): ")

# Convierte las funciones escritas en funciones reales
def f(x):
    return eval(funcion_str)

def f_derivada(x):
    return eval(derivada_str)

# Valor inicial
x0 = float(input("Ingresa el valor inicial (x0): "))

# Parámetros del método
tolerancia = 0.0001
max_iter = 20
iteracion = 0

print("\nIteración |       x       |     f(x)     ")
print("----------------------------------------")

while iteracion < max_iter:
    fx = f(x0)
    fpx = f_derivada(x0)

    # Evitar división entre cero
    if fpx == 0:
        print("Error: derivada igual a cero, no se puede continuar.")
        break

    # Fórmula de Newton-Raphson
    x1 = x0 - fx / fpx

    print(f"{iteracion+1:9d} | {x1:12.4f} | {fx:12.4f}")

    # Verificar si ya se alcanzó la tolerancia
    if abs(x1 - x0) < tolerancia:
        print("\nRaíz aproximada encontrada: {:.4f}".format(x1))
        print("Iteraciones totales:", iteracion + 1)
        break

    x0 = x1
    iteracion += 1

else:
    print("\nNo se encontró la raíz dentro del número máximo de iteraciones.")

