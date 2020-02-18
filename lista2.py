#1
def verifica_natureza():
  numero = float(input("Insira o número que você quer verificar: "))
  if numero > 0:
  	print("seu número é positivo.")
  elif numero < 0:
  	print ("seu número é negativo.")
  else: 
    print(0)
	

#2
# == é quando você compara/ = é quando você atribui um valor fixo/ != é diferente

#float = núemros flutuantes/ int = números inteiros

def verifica_paridade():
	numero = int(input("Insira o número que você quer verificar: "))
	if(numero % 2 == 0):
		print('par')
	else:
		print('impar')
#3

def verifica_maioridade():
  x = float(input("Insira o primeiro número que você quer comparar: "))

  y = float(input("Insira o segundo número que você quer comparar: "))

  if x > y:
    print("O primeiro número é maior que o segundo")
  elif x < y:
    print("O segundo número é maior que o primeiro")
  else:
    print("Os números são iguais")


#4

def verifica_maioridade_3():
  x = float(input("Insira o primeiro número que você quer comparar: "))

  y = float(input("Insira o segundo número que você quer comparar: "))

  z = float(input("Insira o terceiro número que você quer comparar: "))

  if x > y > z:
    print("O primeiro número é maior que o segundo e que o terceiro")
  elif x < y > z:
    print("O segundo número é maior que o primeiro e que o terceiro")
  elif x < y < z:
    print("O terceiro número é maior que o segundo e o primeiro")  
  else:
    print("Os números são iguais")


#5

def verifica_ordena():
  x = float(input("Insira o primeiro número que você quer comparar: "))

  y = float(input("Insira o segundo número que você quer comparar: "))

  z = float(input("Insira o terceiro número que você quer comparar: "))

  if x > y > z:
    if y > z:
      print("Z = {} / Y = {} / X = {}".format(z,y,x))
    else:
      print("Y = {} / Z = {} / X = {}".format(y,z,x))
  elif x < y > z:
    print("O segundo número é maior que o primeiro e que o terceiro")
  elif x < y < z:
    print("O terceiro número é maior que o segundo e o primeiro")  
  else:
    print("Os números são iguais")


#6

def verifica_vogal():
  letra = input("Qual letra deseja verificar? ")
  tupla_vogais = ('a', 'e', 'i', 'o', 'u')
  
  if letra in tupla_vogais:
    print("é vogal")
  else:
    print("não é vogal")

#7

def calcula_novo_salario():
  salario = float(input("Insira seu salário atual: "))
  if salario <= 1000:
    novo_salario = salario*1.3
    print("Seu novo salário será: ", novo_salario)
  elif 1000 < salario <= 2000:
    novo_salario_2 = salario*1.25
    print("Seu novo salário será de: ", novo_salario_2)
  elif 2000 < salario <= 3000:
    novo_salario_3 = salario*1.20
    print("Seu novo salário será de: ", novo_salario_3)
  elif 3000 < salario <= 4000:
    novo_salario_4 = salario*1.15
    print("Seu novo salário será de: ", novo_salario_4)
  else:
    novo_salario_5 = salario*1.10
    print("Seu novo salário será de: ", novo_salario_5)

#8

def verifica_classe_ip():
  ip = float(input("Insira o primeiro octeto do seu endereço de IP: "))
  if 0 < ip <= 127:
    print("Seu IP é classe A")
  elif 127 < ip <= 191:
    print("Seu IP é classe B")
  elif 191 < ip <= 223:
    print("Seu IP é classe C")
  elif 223 < ip <= 239:
    print("Seu IP é classe D")
  else:
    print("Seu IP é classe E")

#9?

def verifica_mes():
  mes = int(input("Insira aqui o número inteiro para verificar o mês correspondente: "))

  meses_lista = [(1, '  January'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'), (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro')]
  meses = dict(meses_lista)
  if mes in meses_lista:
    print(meses[mes])
  else:
    print("Não válido")


verifica_mes()

#10??

def valida_data():
  data = (float(input("Insira aqui a sua data: ")))