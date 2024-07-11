def sumar(num1, num2):
  """
  Función para sumar dos números.

  Parámetros:
    num1 (float): Primer número.
    num2 (float): Segundo número.

  Retorno:
    float: Resultado de la suma.
  """
  resultado = num1 + num2
  return resultado

def restar(num1, num2):
  """
  Función para restar dos números.

  Parámetros:
    num1 (float): Primer número.
    num2 (float): Segundo número.

  Retorno:
    float: Resultado de la resta.
  """
  resultado = num1 - num2
  return resultado

def multiplicar(num1, num2):
  """
  Función para multiplicar dos números.

  Parámetros:
    num1 (float): Primer número.
    num2 (float): Segundo número.

  Retorno:
    float: Resultado de la multiplicación.
  """
  resultado = num1 * num2
  return resultado

def dividir(num1, num2):
  """
  Función para dividir dos números.

  Parámetros:
    num1 (float): Primer número (numerador).
    num2 (float): Segundo número (denominador).

  Retorno:
    float: Resultado de la división.

  Excepciones:
    ZeroDivisionError: Si el denominador (num2) es 0.
  """
  if num2 == 0:
    raise ZeroDivisionError("No se puede dividir por cero.")
  else:
    resultado = num1 / num2
    return resultado

# Programa principal
def main():
  """
  Función principal de la calculadora.
  """
  # Entrada del primer número
  num1 = float(input("Introduce el primer número: "))

  # Entrada del signo de operación
  operacion = input("Introduce el signo de operación (+, -, *, /): ")

  # Entrada del segundo número
  num2 = float(input("Introduce el segundo número: "))

  # Cálculo del resultado
  if operacion == "+":
    resultado = sumar(num1, num2)
  elif operacion == "-":
    resultado = restar(num1, num2)
  elif operacion == "*":
    resultado = multiplicar(num1, num2)
  elif operacion == "/":
    try:
      resultado = dividir(num1, num2)
    except ZeroDivisionError as error:
      print(error)
      return
  else:
    print("Operación no válida.")
    return

  # Mostrar el resultado
  print(f"El resultado de la operación {num1} {operacion} {num2} es: {resultado}")

if __name__ == "__main__":
  main()
