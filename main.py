def fizzbuzz(n):
  # Iterar desde 1 hasta n+1
  for num in range(1, n + 1):
    result = ''
    # Verificar si el número es divisible por 3
    if num % 3 == 0:
      result = result + 'Fizz'
    # Verificar si el número es divisible por 5
    if num % 5 == 0:
      result = result + 'Buzz'
    # Verificar si el número no es divisible ni por 3 ni por 5
    if num % 5 != 0 and num % 3 != 0:
      result = result + str(num)
    # Imprimir la variable de salida
    print(result)

# Llamar a la función fizzbuzz con un argumento de 15
fizzbuzz(15)