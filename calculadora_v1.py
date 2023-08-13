# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def Soma(num1,num2):
    soma =  num1 + num2
    print(num1," + ", num2, " = ", soma)
    
def Subt(num1,num2):
    subt =  num1 - num2
    print(num1," - ", num2, " = ", subt)
        
def Mult(num1,num2):
    mult =  num1 * num2
    print(num1," * ", num2, " = ", mult)
    
def Divi(num1,num2):
    divis =  num1 / num2
    print(num1," / ", num2, " = ", divis)
        
              
print('\nSelecione o número da operação desejada:')

print('1 - Soma\n')
print('2 - Subtração\n')
print('3 - Multiplicação\n')
print('4 - Divisão\n')

opt = int(input('Digite a sua opção(1/2/3/4):'))

num1 = float(input('Digite o primeiro número:'))

num2 = float(input('Digite o segundo número:'))
      

if opt == 1:
     Soma(num1, num2)
             
elif opt == 2:
     Subt(num1, num2)

elif opt == 3:
     Mult(num1, num2)

elif opt == 4:
     Divi(num1, num2)

else:
     print('Você não inseriu um número valido. Insira um número de 1 a 4, por favor!')

      