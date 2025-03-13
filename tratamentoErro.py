print("Divisão \n")
while True:
  try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    conta = n1 / n2
    print(f"O primeiro número ({n1}) dividido pelo segundo número ({n2}) é igual a {conta}")
  except ZeroDivisionError:
    print("Não é possível dividir um número por zero")
  except ValueError:
    print("Por favor digite apenas números inteiros")
  else:
    break
