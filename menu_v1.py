import mod_escaner, module_infodom, module_nmpa, module_pdf, mod_reques, mod_dataimagenes, CrackeoCesar
def menu():
    print("Bienvenido")
    print("Select a module:")
    print("1. Web Scraping")
    print("2. Escaner de puertos")
    print("3. Metadatos PDF")
    print("4. Metadatos imagenes")
    print("5. Crackeo")
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        mod_reques()
    elif choice == 2:
        #agregar para elegir entre dos modulos
        print("1. Escaner de puertos \n 2. Escaner NMPA")
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            mod_escaner()
        else:
            module_nmpa()
    elif choice == 3:
        module_pdf()
    elif choice == 4:
        mod_dataimagenes()
    elif choice == 5:
        CrackeoCesar()
    else:
        print("Invalid choice.")
if __name__== "__main__":
    menu()