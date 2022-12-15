





# Calculadora de Idade em Python

if (resultado <= 0):
    texto = 'Você simplesmente não existe :o'

elif (resultado == 1):
    texto = 'Você é um recém nascido!'

elif (resultado <= 4):
    texto = f'Você é um bêbê de {resultado} anos!'

elif (resultado <= 12):
    texto = f'Você é uma criança de {resultado} anos!'
    
elif (resultado <= 17):
    texto = f'Você é um adolecente de {resultado} anos!'

elif (resultado <= 59): 
    texto = f'Você é um adulto de {resultado} anos!'

else:
    texto = f'Você é um idoso de {resultado} anos!'


print(texto)