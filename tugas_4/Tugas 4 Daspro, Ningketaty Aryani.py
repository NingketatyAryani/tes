def biner_ke_desimal(biner):
    desimal = 0
    panjang = len(biner)
    for i in range(panjang):
        if biner[i] == '1':
            desimal += 2**(panjang - 1 - i)
    return desimal

def desimal_ke_biner(desimal):
    if desimal == 0:
        return '0'
    biner = ''
    while desimal > 0:
        biner = str(desimal % 2) + biner
        desimal //= 2
    return biner

def oktal_ke_desimal(oktal):
    desimal = 0
    panjang = len(oktal)
    for i in range(panjang):
        desimal += int(oktal[i]) * 8**(panjang - 1 - i)
    return desimal

def desimal_ke_oktal(desimal):
    return oct(desimal).replace("0o", "")

def heksadesimal_ke_desimal(heksadesimal):
    return int(heksadesimal, 16)

def desimal_ke_heksadesimal(desimal):
    return hex(desimal).replace("0x", "")

angka = input("Masukkan angka: ")

try:
    # Konversi dari Biner
    if angka.startswith('0b'):
        desimal = biner_ke_desimal(angka[2:])
        print("Desimal:", desimal)
        print("Oktal:", desimal_ke_oktal(desimal))
        print("Heksadesimal:", desimal_ke_heksadesimal(desimal))

    # Konversi dari Oktal
    elif angka.startswith('0o'):
        desimal = oktal_ke_desimal(angka[2:])
        print("Desimal:", desimal)
        print("Biner:", desimal_ke_biner(desimal))
        print("Heksadesimal:", desimal_ke_heksadesimal(desimal))

    # Konversi dari Desimal
    elif angka.isdigit():
        desimal = int(angka)
        print("Biner:", desimal_ke_biner(desimal))
        print("Oktal:", desimal_ke_oktal(desimal))
        print("Heksadesimal:", desimal_ke_heksadesimal(desimal))

    # Konversi dari Heksadesimal
    elif angka.startswith('0x'):
        desimal = heksadesimal_ke_desimal(angka[2:])
        print("Desimal:", desimal)
        print("Biner:", desimal_ke_biner(desimal))
        print("Oktal:", desimal_ke_oktal(desimal))

    else:
        print("Format angka tidak dikenali.")

except ValueError:
    print("Format angka tidak valid.")
