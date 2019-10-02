

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
c = float(input('Digite a terceira nota: '))

med = (a + b + c)/2

if med >= 7.0 :
    print('aprovado')
elif med >= 5.0 and med < 7.0 :
    print('recuperacao')
elif med < 5.0 :
    print('reprovado')

