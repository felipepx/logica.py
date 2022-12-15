operador = input("+: para soma \n-: para subtração \n*: para multiplicação \n/: para divisão\nDigite seu operador: ")
num_one = input('Digite um número: ')
num_two = input('Digite outro número: ')

#soma
if operador == '+':
    resultado = int (num_one) + int (num_two)
    print('O resultado é: ', resultado);
#subtração
if operador == '-':
    resultado = int(num_one) - int(num_two)
    print('O resultado é: ', resultado);
    #subtração
if operador == '*':
    resultado = int(num_one) * int(num_two)
    print('O resultado é: ', resultado);
#divisão
if operador == '/':
    resultado = int(num_one) / int(num_two)
    print('O resultado é: ', resultado);

    input()