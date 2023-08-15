print("Operadores Aritmeticos: Adição (+), Subtração (-), Multiplicação (*), Divisão (/), Divisão inteira (//), Resto da divisão (%), Potenciação (**)")

primeiro_numero = float(input("Digite um numero: "))
operador = str(input("Digite um operador aritmetico: "))
segundo_numero = float(input("Digite outro numero: "))

def resultado():
  if operador == "+":
    resultado = primeiro_numero + segundo_numero
    print("Soma")
  elif operador == "-":
    resultado = primeiro_numero - segundo_numero
    print("Subtração")
  elif operador == "/":
    resultado = primeiro_numero / segundo_numero
    print("Divisão")
  elif operador == "*":
    resultado = primeiro_numero * segundo_numero
    print("Multiplicação")
  elif operador == "**":
    resultado = primeiro_numero ** segundo_numero
    print("Potenciação")
  elif operador == "//":
    resultado = primeiro_numero // segundo_numero
    print("Divisão inteira")
  elif operador == "%":
    resultado = primeiro_numero % segundo_numero
    print("Resto da divisão")   
  else:
    print("Deve colocar um operador valido")
  return resultado

print(resultado())  