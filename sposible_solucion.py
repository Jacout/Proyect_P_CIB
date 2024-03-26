def peticiones(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            if r.headers.get('content-type') == 'application/json':
                personaje = r.json()
                for x, y in personaje.items():
                    print(x, "-", y)
            else:
                print("La respuesta no es JSON")
        else:
            print("El servidor respondió con el código {}".format(r.status_code))
            exit()
    except requests.exceptions.JSONDecodeError as e:
        print(f"fallo en json: {e}")