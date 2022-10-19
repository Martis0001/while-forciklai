#atspausdinti visus keturzenklius skaicius kuriu skaitmenu suma lygi sandaugai
#suskaiciuoti, kiek ju yra
#1000 9999
#1124
#4567 // 1000 ===> 4
#4567 // 100 ===> 45 % 10 ===> 5
#4567 // 100 ===> 456 % 10 ===> 6
#4567 % 10 ===> 7
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