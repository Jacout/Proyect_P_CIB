def Encriptar(Frase):
    FraseEnc = '' #str vacio
    for letra in Frase: #recorro Frase letra por letra
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                FraseEnc += y #fraseEnc.append(y)
                encontrado = True
        if not encontrado: #if encontrado == False
                            # if encontrado != True
            FraseEnc += letra
    return FraseEnc
    
def Desencriptar(Frase):
    FraseDes = ''
    for letra in Frase:
        encontrado = False
        for x,y in abc.items():
            if letra == y:
                FraseDes += x #fraseEnc.append(x)
                encontrado = True
        if not encontrado: #if encontrado == False
            FraseDes += letra
    return FraseDes

#Cifrado César
#La letra más común del abc es la E
# A --> E, B ==> F, C --> G
# Ejemplo: CASA
# GEWE
abc = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
}
print("Menú\n1) Encriptar\n2) Desencriptar\n3) Salir")
x = int(input("Opción: "))
while x != 3:
    if x == 1:
        frase = input('Frase en texto claro: ')
        frase = frase.upper()
        fraseEnc = Encriptar(frase)
        print(fraseEnc)
    elif x == 2:
        frase = input('Frase encriptada: ')
        frase = frase.upper()
        print(Desencriptar(frase))
    else:
        print("Error! Opción no válida")
    print("Menú\n1) Encriptar\n2) Desencriptar\n3) Salir")
    x = int(input("Opción: "))
    
