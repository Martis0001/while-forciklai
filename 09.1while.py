# ivedamas bet koks skaicius
# rasti jo skaitmenu suma 12354



sk = int(input('sk = '))
suma = 0
atsk = 0
ksk = sk
while sk > 0:
    x1 = sk % 10
    atsk = atsk * 10 + x1
    sk = sk//10
print(f'Skaicius {ksk} perrasius atvirksciai gausim {atsk}')