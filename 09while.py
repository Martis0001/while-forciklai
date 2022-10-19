# ivedamas bet koks skaicius
# rasti jo skaitmenu suma 12354



sk = int(input('sk = '))
suma = 0
while sk > 0:
    x1 = sk % 10
    suma += x1 # suma = suma + x1
    sk = sk // 10 # sk //= 10
    atsk = 0
print(f'Skaicius {sk} skaitmenu suma lygi {suma}')


