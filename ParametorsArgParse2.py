import argparse #para argumentos con
parser = argparse.ArgumentParser()
parser.add_argument("-n1", dest="num1", type=int) #primer argumento
parser.add_argument("-n2", dest="num2", type=int) #segundo argumento
parser.add_argument("-n3", dest="num3", type=int) #tercer argumento
params = parser.parse_args()
prom = (params.num1 + params.num2 + params.num3)/3
print("Promedio: ", prom)


#se ejecuta con script -n1 valor -n2 valor -n3 valor