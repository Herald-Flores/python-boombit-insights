# Función para calcular la serie de Fibonacci hasta el número n
def fibonacci(n):
  # Caso base: si n es 0 o 1, retornar n
  if n < 2:
    return [n]

  # Variables iniciales para los dos primeros números de la serie
  anterior, actual = 0, 1
  count = 0
  serie = []
  
  # Ciclo para calcular el número Fibonacci para n > 1 y generar la serie
  while count < n:
    serie.append(anterior)
    siguiente = anterior + actual
    anterior = actual
    actual = siguiente
    count += 1
    
  # Retornar la serie de Fibonacci hasta el número n
  return serie


# Solicitar al usuario el valor de n
n = int(input("Ingrese el valor de n: "))

# Calcular la serie de Fibonacci hasta el número n
resultado = fibonacci(n)

# Mostrar el resultado
print("La serie de Fibonacci hasta el número", n, "es: ")
print(resultado)