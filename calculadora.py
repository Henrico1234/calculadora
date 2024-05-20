print("querido usuario selecione a opção desejada")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

op = int(input("Digite sua opção(1/2/3/4)"))

n1= float(input("digite o primeiro numero"))

n2= float(input("digite o segundo numero"))

if op == 1:
    resultado = n1 + n2
    
elif op == 2:
    resultado = n1 - n2

elif op == 3:
    resultado = n1 * n2

elif op == 4:
    resultado = n1 / n2

# Exibição do resultado
if operacao and not isinstance(resultado, str):  # Se a operação é válida e resultado não é uma mensagem de erro
    print(f"{n1} {operacao} {n2} = {resultado}")
else:
    print(resultado)



