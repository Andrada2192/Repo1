piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca nr este par printam acest lucru
# altfel printam impar
nr = 3
# ce inseamna par => se imparte la 2
# ce inseamna ca se imparte la 2! ne da restul 0
if nr % 2 == 0:
   print('nr par')
else:
   print('impar')

# este un numar pozitiv?
if (nr > 0):
    print('pozitiv')
else:
    print('nr nu este pozitiv')

# daca are sub 18 ani, nu poate paria

# if, else if, else
# cum ne saluta robotelul in functie de ora?

#luam date de la tastatura
#ne asiguram ca sunt transformate din str in int
# ora = int(input('Introdu ora'))
# if ora < 0:
#     print('ora invalida, ora negativa')
# elif ora <= 11:
#     print('buna dimineata')
# elif ora <= 18:
#     print('buna ziua')
# elif ora <= 21:
#     print('buna seara')
# elif ora <= 24:
#     print('noapte buna')
# else:
#     print('ora invalida, ora mai mare decat 24')
# CTRL + /


#switch
# robotel telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiune == 1:
    print('ati ales ro')
elif optiune == 2:
    print('ati ales eng')
else:
    print('nu am identificat optiunea, mai incearca')
