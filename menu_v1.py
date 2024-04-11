def module1():
    import module1
    module1.function1()

def module2():
    import module2
    module2.function2()

def module3():
    import module3
    module3.function3()

def module4():
    import module4
    module4.function4()

def module5():
    import module5
    module5.function5()

def menu():
    print("Bienvenido")
    print("Select a module:")
    print("1. Web Scraping")
    print("2. Escaner de puertos")
    print("3. Metadatos PDF")
    print("4. Metadatos imagenes")
    print("5. NMAP")
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        module1()
    elif choice == 2:
        module2()
    elif choice == 3:
        module3()
    elif choice == 4:
        module4()
    elif choice == 5:
        module5()
    else:
        print("Invalid choice.")
if __name__== "__main__":
    menu()