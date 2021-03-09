import math
print('Zadanie 1')
a, b = 'To zmienna łańcuchowa\n', "Zmienna łańcuchowa\tnr 2"
c, d = 6, 122  # zmienne integer
e, f = 2.5, 72.25  # zmienne float
g, h = 5 + 3j, -1 + 2j  # zmienne complex

print(a + b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

print('Zadanie 2')
dodawanie = c + d
odejmowanie = f - e
mnozenie = c * e
dzielenie = d / f
potega = c ** e
reszta = d % c

print(dodawanie)
print(odejmowanie)
print(mnozenie)
print(dzielenie)
print(potega)
print(reszta)

print('Zadanie 3')
print(math.exp(10))
print((math.log10(5+math.sin(8)**2))**1/6)

print('Zadanie 4')
imie = 'MICHAL'
nazwisko = 'LUKASZEWICZ'
print(str.capitalize(imie))
print(str.capitalize(nazwisko))

print('Zadanie 5')
tekst = 'Always look on the bright side of life, fiu fiu, fiu fiu fiu fiu fiu fiu'
print(tekst.count('fiu'))

print('Zadanie 6')
indeksy = 'Zmienna do zadania nr 6'
print(indeksy[1])
print(indeksy[22])

print('Zadanie 7')
print(indeksy.split())
