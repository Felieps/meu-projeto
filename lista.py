#part1
while True:
    try:
        num = int(input('digite um número: '))
        num2 = int(input('digite outro número: '))
        break
    except ValueError:
        print('isto não é um número, tente novamente')
resultado = num + num2
print(f'{resultado}')
#part2
while True:
    try:
        n = int(input('digite a primeira nota: '))
        n2 = int(input('digite a segunda nota: '))
        n3 = int(input('digite terceira nota: '))
        break
    except ValueError:
        print('isto não é um número, tente novamente')
resultado = (n+n2+n3)/3
print(f'{resultado}')
#part3
while True:
    try:
        B = int(input('digite a base da área: '))
        H = int(input('digite a altura da área: '))
        break
    except ValueError:
        print('isto não é um número, tente novamente')
resultado = B*H
print(f'{resultado}cm²')
#part4
while True:
    try:
        TC = int(input('digite a temperatura em °C: '))
        break
    except ValueError:
        print('isto não é um número, tente novamente')
resultado = (1.8*TC)+32
print(f'{resultado}°F')
#part5
while True:
    try:
        peso = int(input('digite o seu peso: '))
        altura = float(input('digite sua altura: '))
        break
    except ValueError:
        print('isto não é um número, tente novamente')
resultado = peso/(altura**2)
print(f'{resultado:.2f}')
#part6
while True:
    try:
        Nu = int(input('digite o valor: '))
        break
    except ValueError:
        print('isto não é um número, tente novamente')
DB = (Nu*2)
TP = (Nu*3)
print(f'{DB} este é o dobro, {TP} este é o triplo.')
#part7
while True:
    try:
        preço = float(input('digite o valor do produto: '))
        desconto = float(input('informe o desconto: '))
        break
    except ValueError:
        print('isto não é um número, tente novamente')
calc = preço*desconto/100
resultado = preço - calc
print(f'R${resultado}')
#part8
while True:
    try:
        salario = float(input('digite seu salário R$: '))
        aumento = float(input('digite o aumento %: '))
        break
    except ValueError:
        print('isto não é um número, tente novamente')
percentual = (aumento/100)
acrescimo = percentual*salario
resultado = salario+acrescimo
print(f'salário R$:{resultado:.2f}')
#part9
while True:
    try:
        Moeda = float(input('digite o valor para conversão: '))
        break
    except ValueError:
        print('isto não é um número, tente novamente')
resultado = Moeda/5.50
print(f'${resultado:.2f}')
#part10

