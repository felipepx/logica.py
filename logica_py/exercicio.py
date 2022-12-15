from string import ascii_letters

# caracteres que eu preciso 

validos = ascii_letters + ' áéíóú'
while True:
    nome_aluno = input('Digite seu nome: ')
    
    if nome_aluno == ' ':
        print('O primero carácter não pode ser um espaço!')


    elif all(c in validos for c in nome_aluno):


        break # quebra o loop
    
    
    else:
        print('Por favor digite um nome válido (somente letras e espaços)')

    


try:

    nota_media = 6
    nota_prova = 10
    nota_aluno = int(input(f'Olá {nome_aluno}, digite a nota da sua prova: '))


except (ValueError , TypeError):

    print('Só é permitido números. Por favor, insira um valor válido! :(')


except (KeyboardInterrupt):

    print('\nO usuário preferiu não informar os dados! :(')




else:

    if nota_aluno > nota_prova:

        print('A nota máxima da prova é 10.\nPor favor, insira um valor válido! :(') 
    

    elif nota_aluno >= nota_media:
    
        print(f'Parabéns {nome_aluno}, você está APROVADO')


    elif nota_aluno < nota_media:
    
        print(f'Sinto muito {nome_aluno}, você está REPROVADO')

    
finally:
   print (f'puf puf')