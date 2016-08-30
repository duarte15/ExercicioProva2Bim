n = int(input("Informe a quantidade de termos desejados:" ))

a = 1

b = 1

print(a)

print(b)


for i in range(n-2):

    c = a+b

    aux = a

    a = c

    b = aux

    print(c)