# List link: https://wiki.python.org.br/EstruturaSequencial

#----------------------------------------------------------------

# Questão 1

print('Olá mundo')

#----------------------------------------------------------------

# Questão 2

a = input("Digite seu número: ")
print("O número informado foi:", a)

#----------------------------------------------------------------

# Questão 3

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print("A soma é: ", a + b)

#----------------------------------------------------------------

# Questão 4

a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))
d = float(input("Digite a quarta nota: "))
e = float(a + b + c + d)
final = float(e/4)
print("A média é:", final)

#----------------------------------------------------------------

# Questão 5

a = float(input("Digite quantos metros deseja converter: "))
b = float(a*100)
print("O seu valor em cm é:", b)

#----------------------------------------------------------------

# Questão 6

raio = float(input("Digite o raio do círculo a ser calculado: "))
diametro = float(raio*raio)
area = float(diametro*3.14)
print("Área =", area)

#----------------------------------------------------------------

# Questão 7

l = (float(input("Digite o lado do quadrado: ")))
a = l*l
print("Area quadrado: ",a)
print("Area quadrado (dobro): ",a*2)

#----------------------------------------------------------------

# Questão 8

x = (float(input("Valor ganho, horas trabalhadas: ")))
y = (float(input("Horas que trabalha no mês: ")))
re = x*y
print("total do seu salário no referido mês: " , re)
print("")

#----------------------------------------------------------------

# Questão 9

f = (float(input("Digite os graus em fahrenheit: ")))
r = 5*((f-32)/9)
print("Graus convertidos em c° = ", r, "c°")
print("")

#----------------------------------------------------------------

# Questão 10

c = (float(input("Coloque os graus celcius: ")))
r = ((c/5)*9)+32
print("Graus convertidos em f° = ", r, "f°")
print("")

#----------------------------------------------------------------

# Questão 11

x = (int(input("Número 1: ")))
y = (int(input("Número 2: ")))
w = (float(input("Número 3 float: ")))
print("O produto do dobro do primeiro com metade do segundo: " , (2*x) * (y/2))
print("A soma do triplo do primeiro com o terceiro: " , (3*x) + w)
print("O terceiro elevado ao cubo: " , w**3)
print("")

#----------------------------------------------------------------

# Questão 12

print("12) ")
a = (float(input("Altura: ")))
peso = (72.7*a) - 58
print(" O seu peso ideal é: " , peso)

#----------------------------------------------------------------

# Questão 13

sexo = (str(input("Seu sexo, homem(h), mulher(m) = ")))
a = (float(input("Altura = ")))
if  ('h' in sexo) :
    print("Senhor, seu peso ideal : " , (72.7 * a) - 58)
if  ('m' in sexo) :
    print("Senhora, seu peso ideal: " , (62.1 * a) - 44.7)
print("")

#----------------------------------------------------------------

# Questão 14

print("Valor do peixe = 20 reais por kg")
kgpeixe = (float(input("Kg do peixe: ")))
precopeixe = kgpeixe * 20
exced = kgpeixe - 50
if(kgpeixe > 50):
    precopeixe += kgpeixe*4
    multa = precopeixe - (exced*4)
else:
    multa = 0
    precopeixe = 20*kgpeixe
print("Valor a ser pago do peixe: ", precopeixe)
print("Multa: " , multa)
print("Excesso do peixe: " , exced)
print(" ")

#----------------------------------------------------------------

# Questão 15

x = (float(input("Valor ganho, horas trabalhadas = ")))
y = (float(input("Horas que trabalha no mes = ")))
re = x*y
print("Total do seu salário no referido mes = " , re)
print("")
print("Salário bruto: " , re)
inss = (re*8)/100
print ("Valor para o INSS: " , inss)
sind = (re*5)/100
print ("Valor para o sindicato: ",sind)
ir = (re*11)/100
rliquido = re - sind - inss - ir
print( "Perda total de valores: ", rliquido)
print("")

#----------------------------------------------------------------

# Questão 16

x = float(input("Quantidade em metros a ser pintado: "))
quant = x/3
preco = quant*(80/18)
latas = x/54
print ("Preco a ser pago: ",preco, " R$")
print("Quantidade de latas para ser usadas: ",latas)
print("")

#----------------------------------------------------------------

# Questão 17

x = float(input("Quantidade em metros para ? "))
quant= x/6
p1 = quant*(80/18)
p2 = quant*(25/3.6)
latas1 = x/54
latas2 = x/10.8
x = input(print("Qual vai usar ? Escolha entre (A), (B) ou (C) "
                "\n A)Latas grandes "
                "\n B)Latas Pequenas "
                "\n C)Todas"))
if (x == 'A'):
    print("Quantidade de latas a serem usadas: ",latas1)
    print ("Preco a ser pago: ",p1, " R$")
elif (x == 'B'):
    print("Quantidade de latas a serem usadas: ",latas2)
    print ("Preco a ser pago: ",p2, " R$")
else:
    print("")

#----------------------------------------------------------------

# Questão 18

x = float(input("Tamanho do arquivo (em MB) "))
y = float(input("Velocidade do link (em Mbps) "))
re = (x/(y/8))
print ("Tempo aproximado = ",re/60)

#----------------------------------------------------------------