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
  resultado = None  # Variable para almacenar el resultado acumulado

  while True:
    try:
      # Si no hay resultado previo, solicitar el primer número
      if resultado is None:
        resultado = float(input("Introduce el primer número: "))

      # Solicitar el símbolo de operación
      operacion = input("Introduce el signo de operación (+, -, *, /): ")

      # Solicitar el siguiente número
      num2 = float(input("Introduce el siguiente número: "))

      # Calcular el resultado
      if operacion == "+":
        resultado = sumar(resultado, num2)
      elif operacion == "-":
        resultado = restar(resultado, num2)
      elif operacion == "*":
        resultado = multiplicar(resultado, num2)
      elif operacion == "X":
        break
      elif operacion == "/":
        try:
          resultado = dividir(resultado, num2)
        except ZeroDivisionError as error:
          print(error)
          continue
      else:
        print("Operación no válida.")
        continue

      # Mostrar el resultado acumulado
      print(f"Resultado actual: {resultado}")

    except ValueError:
      print("Entrada no válida. Introduce un número.")

# Ejecutar el programa principal
if __name__ == "__main__":
  main()
