
# inclusividade

nome = str(input('Olá, qual o seu nome? '))
sexo = int(input('Qual sexo você se identifica?\nDigite:\n(1) para Masculino\n(2) para Feminino\n(3)para Outro\n* '))
pronome = int(input('Qual seu pronome?\nDigite:\n(1) para ELE/DELE\n(2) para ELA/DELA\n(3) para ELU/DELU\n* '))

# pronome, genitivos 1 e 2 

if (pronome == 1):
     genitivo = 'o'
     genitivo2 = 'a'
     artigo2 = 'um'
elif (pronome == 2):
    genitivo = 'a'
    artigo2 = 'uma'
else:
    genitivo2 = ''
    genitivo = 'x'
    artigo2 = 'um'





text2 = (f'Olá {nome}, bem vind{genitivo} a Morphelse. Sua calculadora de idade')

print(text2)


ano_atual = int(input('Qual o ano atual? '))
ano_nascimento = int(input('Qual o ano do seu nascimento? '))
idade = (ano_atual - ano_nascimento)


# genero

if (sexo == 1):
    genero = 'homem'

elif (sexo == 2):
    genero = 'mulher'

else: 
    genero = 'pessoa'


# artigo
if (genero == 'homem'):
    genitivo3 = 'o'
    artigo = 'um'
 
elif (genero == 'mulher'):
    artigo = 'uma'
    genitivo3 = 'a'


else:
    genitivo3 = 'a'
    artigo = 'uma'
    artigo2 = 'um'





# Calculadora de Idade em Python

if (idade <= 0):
    texto = f'Desculpe {nome}, mas você simplesmente não existe :('

elif (idade <= 1):
    texto = f'Olá {nome}, você é um recém nascido!'

elif (idade <= 4):
    texto = f'Olá {nome}, você é um{genitivo2} bêbê de {idade} anos!'

elif (idade <= 12):
    texto = f'Olá {nome}, você é uma criança de {idade} anos!'
    
elif (idade <= 17):
    texto = f'Olá {nome}, você é {artigo2} adolecente de {idade} anos!'

elif (idade <= 59): 
    texto = f'Olá {nome}, você é {artigo} {genero} adult{genitivo3} de {idade} anos!'

else:
    texto = f'Olá {nome}, você é um{genitivo3} idos{genitivo} de {idade} anos!'


print(texto)