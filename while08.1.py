#atspausdinti visus keturzenklius skaicius kuriu skaitmenu suma lygi sandaugai
#suskaiciuoti, kiek ju yra
#100 9999
#1124
#456 // 1000 ===> 0
#456 // 100 ===> 4 % 10 ===> 4
#456 // 100 ===> 45 % 10 ===> 5
#456 % 10 ===> 6

sk1 = 100
sk = 1000
kiek = 0

while sk<=9999:
    x1 = sk // 1000
    x2 = sk // 100 % 10
    x3 = sk // 10  % 10
    x4 = sk % 10
    suma = x1+x2+x3+x4 
    sd = x1*x2*x3*x4 
    if suma == sd:
        print(sk,end=" ")
        kiek+=1
    sk += 1
print(f'/nJu yra {kiek}')

while sk<=100:
    y1 = sk1 // 100
    y2 = sk1 // 100 % 1
    y3 = sk1 % 10
    suma = y1+y2+y3
    sd = y1*y2*y3 
    if suma == sd:
        print(sk,end=" ")
        kiek+=1
    sk += 1
print(f'/nJu yra {kiek}') 