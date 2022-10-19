#Petriukas ir jo pazymiai. rasti vidurki. didziausi- maziausi pazymiai
#problema neturim masyvo
kiekis =int(input('Kiek Petriukas turi pazymiu'))
suma = 0
maz = None
did = None
kelintas = 0

while kelintas < kiekis:
    paz = int(input(f'Iveskite {kelintas+1} pazimi'))
    if paz<1 or paz>10:
        print('Neteisingas pazimys. kartokite ivedima')
        continue
    if kelintas == 0:
        did = paz
        maz = paz
    else:
        if did< paz:
            did = paz
        if maz > paz:
           maz = paz    
    kelintas += 1
    suma = suma + paz
    vidurkis = suma / kiekis
    print(f'petriuko vidurkis {vidurkis}')
    print(f'Didziausias {did}, o maziausias {maz}')